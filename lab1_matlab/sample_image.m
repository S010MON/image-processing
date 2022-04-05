close all; clear all; clc

x = imread('eggs.png');
figure;imagesc(x);

[n1 n2 n3] = size(x);
xs = x(1:100:n1, 1:100:n2,:);

figure;imagesc(xs)
