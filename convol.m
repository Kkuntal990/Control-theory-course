t = linspace(0.000001,10,10000);
for i=1:10000
    a(i) = sin(t(i))/(pi*t(i));
end
b = ones(1,10000);

c = conv(a,b);
plot(c)