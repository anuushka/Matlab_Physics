g=9.81; % acceleration of gravity
u_o=60; % initial velocity
t=0:0.1:15; % discrete time span
s=u_o*t-(g/2)*t.^2; % compute position values
plot(t,s)
title('Vertical motion under gravity');
xlabel('Time (s)');
ylabel('Position (m)');
grid on;
disp([t' s']) % display time and position values