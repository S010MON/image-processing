function [xq1, xq2] = quantizeimage(q1, q2, xg)

% Find range of grayscale image values
m1 = min(xg(:)); m2 = max(xg(:));
range_xg = m2-m1;

% Find interval length for desired quantization levels
d1 = range_xg/q1;
d2 = range_xg/q2;

%Manual estimation of quantization levels for "imquantize" function:
l1 = m1:d1:m2; l1 = l1(2:end-1);
l2 = m1:d2:m2; l2 = l2(2:end-1);

%Alternative: automatic estimation of quantization levels for "imquantize" function:
t1 = multithresh(xg,9);
t2 = multithresh(xg,1);

% You can replace l1, l2 with the automatically calculated t1, t2
xq1 = imquantize(xg,l1);
xq2 = imquantize(xg,l2);

