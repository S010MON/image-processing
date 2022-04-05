close all; clear all; clc

% Read a color image, resize if needed
x00 = imread('eggs.jpg'); x0 = imresize(x00,0.25);

% Convert color image to gray and double values
xg0 = rgb2gray(x0); xg = double(xg0);

% Number of quantization levels: 10 or 2:
q1 = 10; q2 = 2;

[xq1, xq2] = quantizeimage(q1, q2, xg);

figure;imagesc(xg);colormap gray;
figure;imagesc(xq1);colormap gray;
figure;imagesc(xq2);colormap gray;