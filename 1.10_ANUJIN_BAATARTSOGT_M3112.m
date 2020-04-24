%problem 1.10

%vertical projectile
x0=0;
y0=0;
theta=pi*(60/180); %angle
g=10; % acceleration of gravity
u_o=25; % initial velocity
t=0:0.1:1.7; % discrete time span
xdot0=u_o*cos(theta);%compute range
ydot0=u_o*sin(theta);

%plot vertical projectile
s=u_o*t-(g/2)*t.^2; % compute position values
plot(t,s)

%plot angular projection
hold on
x=xdot0*t+x0;
y2=-(g/2)*t.^2+ydot0*t;
plot(t,y2) %plot angular projectile
hold off

title('Projectile of two bodies');
xlabel('Time (s)');
ylabel('Position (m)');
legend('vertical projectile', 'horizontal projectile','Location', 'SouthEast')
grid on;
disp([t' s']) % display time and position values
disp([t' y2']) % display time and position values