-- Create the Employee table to store employee information
CREATE TABLE Employee (
    id SERIAL PRIMARY KEY, -- Unique identifier for each employee
    first_name VARCHAR NOT NULL, -- First name of the employee
    last_name VARCHAR NOT NULL, -- Last name of the employee
    email VARCHAR UNIQUE NOT NULL, -- Email address of the employee (must be unique)
    hire_date DATE NOT NULL, -- Date when the employee was hired
    department VARCHAR -- Department in which the employee works
);

-- Create the Benefit table to store information about different benefits
CREATE TABLE Benefit (
    id SERIAL PRIMARY KEY, -- Unique identifier for each benefit
    benefit_name VARCHAR NOT NULL, -- Name of the benefit
    description TEXT NOT NULL, -- Description of the benefit
    external_links VARCHAR -- External links related to the benefit
);

-- Create the EmployeeBenefits table to associate employees with benefits
CREATE TABLE EmployeeBenefits (
    id SERIAL PRIMARY KEY, -- Unique identifier for each employee benefit
    employee_id INT NOT NULL, -- ID of the employee
    benefit_id INT NOT NULL, -- ID of the benefit
    start_date DATE NOT NULL, -- Start date of the benefit for the employee
    end_date DATE NOT NULL, -- End date of the benefit for the employee
    FOREIGN KEY (employee_id) REFERENCES Employee(id), -- Foreign key constraint to link with Employee table
    FOREIGN KEY (benefit_id) REFERENCES Benefit(id) -- Foreign key constraint to link with Benefit table
);

-- Create the StockGrant table to store information about stock grants
CREATE TABLE StockGrant (
    id SERIAL PRIMARY KEY, -- Unique identifier for each stock grant
    employee_id INT NOT NULL, -- ID of the employee
    grant_date DATE NOT NULL, -- Date when the stock grant was given
    cliff_date DATE NOT NULL, -- Date when the stock grant becomes fully vested
    shares_allocated INT NOT NULL, -- Number of shares allocated in the stock grant
    vesting_schedule VARCHAR NOT NULL, -- Vesting schedule for the stock grant
    exercise_price DECIMAL NOT NULL, -- Exercise price of the stock grant
    FOREIGN KEY (employee_id) REFERENCES Employee(id) -- Foreign key constraint to link with Employee table
);

-- Create the VestingRecord table to track the vesting of stock grants
CREATE TABLE VestingRecord (
    id SERIAL PRIMARY KEY, -- Unique identifier for each vesting record
    stock_grant_id INT NOT NULL, -- ID of the stock grant
    vesting_date DATE NOT NULL, -- Date when the shares were vested
    shares_vested INT NOT NULL, -- Number of shares vested on the vesting date
    shares_remaining INT NOT NULL, -- Number of shares remaining after vesting
    FOREIGN KEY (stock_grant_id) REFERENCES StockGrant(id) -- Foreign key constraint to link with StockGrant table
);
