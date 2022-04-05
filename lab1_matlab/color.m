
close all; clear all;

x = imread('colorcabins.jpeg');

r = x(:,:,1);
g = x(:,:,2);
b = x(:,:,3);

figure;imshow(x); title('original image')
figure;imshow(r); title('Red image component')
figure;imshow(g); title('Green image component')
figure;imshow(b); title('Blue image component')