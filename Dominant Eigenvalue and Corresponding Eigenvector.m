% MATLAB Code for Power Method

% Name: Adithya Sajeevan
% Roll No.: 2103302

A = input('Enter the matrix: '); %Inputs the n*n matrix
x = input('Enter initial guess: '); %Inputs the n*1 initial guess
eps1 = input('Enter tolerance error: '); %Input tolerance error
nmax = input('Enter maximum number of iterations required: '); %Inputs maximum number of iterations

%Calling function to perform power method
[powerval, powervec] = power(A, x, eps1, nmax);

disp('Dominant eigenvalue calculated using power method: ');
disp(powerval); %Displays eigenvalue found using power method
disp('Corresponding eigenvector: ');
disp(powervec); %Displays corresponding eigenvector

%Code to find dominant eigenvalue and corresponding eigenvector using
%built-in function
E = eig(A);
domval = E(abs(E) == max(abs(E)));
domval = domval(1, 1);
[V, D] = eig(A);
[posx, posy] = find(D == domval);
domvec = V(:, posx);

disp('Dominant eigenvalue calculated using in-built function: ');
disp(domval); %Displays eigenvalue found using in-built function
disp('Corresponding eigenvector: ');
disp(domvec); %Displays corresponding eigenvector

%Power method function definition
function [lambda1, v] = power(A, x, eps1, nmax)
    lambda1 = 0;
    nsteps = 1;
    err = 1;
    state = 1;

    while ((nsteps <= nmax) & (state == 1))
        y = A*x;
        [r, m] = max(abs(y));
        mu1 = r;
        dlamb = abs(lambda1 - mu1);
        y = (1/mu1)*y;
        dvect = norm(x - y);
        err = max(dlamb, dvect);

        x = y;
        lambda1 = mu1;
        state = 0;
        if (err > eps1)
            state = 1;
        end
        nsteps = nsteps + 1;
    end

    v = x;
end