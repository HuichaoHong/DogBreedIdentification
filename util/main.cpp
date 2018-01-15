/*
 *author:         honghuichao
 * data :         2018.01.08
 *
 */
#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <fstream>
#include <dirent.h>
#include <sys/types.h>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <json/json.h>
//--fix---
int parse(std::string src,std::string dst);
int batch_parse(std::string src,std::string dst);

int main(int argc,char** argv)
{

    if(argc<2){

        std::cout<<"please input the param!"<<std::endl;
        return  0;

    }
    batch_parse(argv[1],argv[2]);
    return 0;
}

int batch_parse(std::string src,std::string dst)
{

    DIR *dir=NULL;
    struct dirent* pDir=NULL;
    dir=opendir(src.c_str());
    if(dir == NULL)
        std::cout<<"Error! can't open this dir"<<std::endl;
    else{
        while(1)
        {
            pDir = readdir(dir);
            if (pDir == NULL) break;
            if (pDir->d_type == DT_REG)
            {
                std::string tmp=src;
                tmp=src+"/"+pDir ->d_name;
                std::cout<<src<<std::endl;
                parse(tmp,dst);

            }

        }
    }
    closedir(dir);
}


int parse(std::string src,std::string dst)
{
    Json::Reader reader;
    Json::Value root;
    std::vector<std::vector<cv::Point> > points;
    points.resize(1);//the

    std::ifstream is;
    is.open (src.c_str(), std::ios::binary );

    if(is==NULL)
    {
        std::cout<<"could not read file or no such file exist"<<std::endl;
        return -1;
    }

    reader.parse(is,root);
    std::cout<<"the sum of points is: "<<root["shapes"][0]["points"].size()<<std::endl;
    points[0].resize(root["shapes"][0]["points"].size());


    for (int i = 0; i <root["shapes"][0]["points"].size(); ++i)
    {

        points[0][i].x=root["shapes"][0]["points"][i][0].asDouble();
        points[0][i].y=root["shapes"][0]["points"][i][1].asDouble();

    }

    std::cout<<points.size();

    std::string src_image=root["imagePath"].asString();
    dst=dst+src_image.substr(src_image.find_last_of("/"),src_image.size());
    cv::Mat tmp=cv::imread(src_image.c_str());
    //std::cout<<tmp.rows<<std::endl;
    cv::Mat ret=cv::Mat::zeros(tmp.rows,tmp.cols,CV_8UC1);

    cv::drawContours(ret,points,0,cv::Scalar(255),CV_FILLED);
    cv::imshow("ret",ret);
    cv::waitKey(100);
    cv::imwrite(dst,ret);
    std::cout<<"finished: "<<std::endl;

    return  1;

}