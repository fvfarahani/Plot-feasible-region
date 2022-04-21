# plot-feasible-region

Plotting feasible region for a linear optimization model. 

Here, two scenarios where integer constraints have been relaxed for computational perspectives. After solving each scenario, Fenchel Decomposition (FD) cut is generated to cut off all non integer solution points from the feasible region. 

Scenario 1:

<img src="https://latex.codecogs.com/svg.image?\begin{align*}\begin{split}\phi(x^1,\omega_1)=\text{Min&space;}&space;&&space;-2&space;y_1&space;(\omega_1)&space;-2&space;y_2(\omega_1)&space;\\\text{&space;s.t.&space;}&space;&&space;y_1(\omega_1)&space;-&space;y_2(\omega_1)&space;\geq&space;-0.6\\&&space;&space;-y_1(\omega_1)&space;-&space;y_2(\omega_1)&space;\geq&space;-1.2&space;&plus;&space;0.5x^1\\&&space;&space;-y_1(\omega_1)&space;\geq&space;-1\\&&space;&space;-y_2(\omega_1)&space;\geq&space;-1\\&&space;y_1&space;(\omega_1),&space;y_2&space;(\omega_1)&space;\geq&space;0.\end{split}\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}\begin{split}\phi(x^1,\omega_1)=\text{Min } & -2 y_1 (\omega_1) -2 y_2(\omega_1) \\\text{ s.t. } & y_1(\omega_1) - y_2(\omega_1) \geq -0.6\\& -y_1(\omega_1) - y_2(\omega_1) \geq -1.2 + 0.5x^1\\& -y_1(\omega_1) \geq -1\\& -y_2(\omega_1) \geq -1\\& y_1 (\omega_1), y_2 (\omega_1) \geq 0.\end{split}\end{align*}" />

Scenario 2:

<img src="https://latex.codecogs.com/svg.image?\begin{align*}\begin{split}\phi(x^1,\omega_2)=\text{Min&space;}&space;&&space;-2&space;y_1&space;(\omega_2)&space;-2&space;y_2(\omega_2)&space;\\\text{&space;s.t.&space;}&space;&&space;y_1(\omega_2)&space;-&space;y_2(\omega_2)&space;\geq&space;-0.6\\&&space;&space;-y_1(\omega_2)&space;-&space;y_2(\omega_2)&space;\geq&space;-1.4&space;&plus;&space;0.5x^1\\&&space;&space;-y_1(\omega_2)&space;\geq&space;-1\\&&space;&space;-y_2(\omega_2)&space;\geq&space;-1&space;\\&&space;y_1&space;(\omega_2),&space;y_2&space;(\omega_2)&space;\geq&space;0.\end{split}\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}\begin{split}\phi(x^1,\omega_2)=\text{Min } & -2 y_1 (\omega_2) -2 y_2(\omega_2) \\\text{ s.t. } & y_1(\omega_2) - y_2(\omega_2) \geq -0.6\\& -y_1(\omega_2) - y_2(\omega_2) \geq -1.4 + 0.5x^1\\& -y_1(\omega_2) \geq -1\\& -y_2(\omega_2) \geq -1 \\& y_1 (\omega_2), y_2 (\omega_2) \geq 0.\end{split}\end{align*}" />

Scenarios after adding FD cut to the relaxed model:

Scenario 1:

<img src="https://latex.codecogs.com/svg.image?\begin{align*}\begin{split}\phi(x^1,&space;\omega_1)=\text{Min&space;}&space;&&space;-2&space;y_1(\omega_1)&space;-2&space;y_2(\omega_1)&space;\\\text{&space;s.t.&space;}&space;&&space;y_1&space;(\omega_1)&space;-&space;y_2(\omega_1)&space;\geq&space;-0.6\\&&space;&space;-y_1(\omega_1)&space;-&space;y_2(\omega_1)&space;\geq&space;-1.2&space;&plus;&space;0.5x\\&&space;&space;-y_1(\omega_1)&space;\geq&space;-1\\&&space;&space;-y_2(\omega_1)&space;\geq&space;-1\\&&space;&space;-y_1(\omega_1)&space;-&space;y_2(\omega_1)&space;\geq&space;-1&space;&plus;x\end{split}\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}\begin{split}\phi(x^1, \omega_1)=\text{Min } & -2 y_1(\omega_1) -2 y_2(\omega_1) \\\text{ s.t. } & y_1 (\omega_1) - y_2(\omega_1) \geq -0.6\\& -y_1(\omega_1) - y_2(\omega_1) \geq -1.2 + 0.5x\\& -y_1(\omega_1) \geq -1\\& -y_2(\omega_1) \geq -1\\& \textcolor{red} {-y_1(\omega_1) - y_2(\omega_1) \geq -1 +x}\end{split}\end{align*}" />

 Scenario 2:

<img src="https://latex.codecogs.com/svg.image?\begin{align*}\phi(x^1,&space;\omega_2)=\text{Min&space;}&space;&&space;-2&space;y_1(\omega_2)&space;-2&space;y_2(\omega_2)&space;\\\text{&space;s.t.&space;}&space;&&space;y_1&space;(\omega_2)&space;-&space;y_2(\omega_2)&space;\geq&space;-0.6\\&&space;&space;-y_1(\omega_2)&space;-&space;y_2(\omega_2)&space;\geq&space;-1.4&space;&plus;&space;0.5x\\&&space;&space;-y_1(\omega_2)&space;\geq&space;-1\\&&space;&space;-y_2(\omega_2)&space;\geq&space;-1\\&&space;&space;-y_1(\omega_2)&space;-&space;y_2(\omega_2)&space;\geq&space;-1&space;&plus;x\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}\phi(x^1, \omega_2)=\text{Min } & -2 y_1(\omega_2) -2 y_2(\omega_2) \\\text{ s.t. } & y_1 (\omega_2) - y_2(\omega_2) \geq -0.6\\& -y_1(\omega_2) - y_2(\omega_2) \geq -1.4 + 0.5x\\& -y_1(\omega_2) \geq -1\\& -y_2(\omega_2) \geq -1\\& -y_1(\omega_2) - y_2(\omega_2) \geq -1 +x\end{align*}" />


