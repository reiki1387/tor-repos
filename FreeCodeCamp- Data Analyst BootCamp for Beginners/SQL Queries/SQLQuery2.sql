--SELECT *
--FROM [SQL Tutorial].dbo.EmployeeDemographics
--Full Outer Join [SQL Tutorial].dbo.WareHouseEmployeeDemographics
--	ON EmployeeDemographics.EmployeeID = WareHouseEmployeeDemographics.EmployeeID

--SELECT *
--FROM [SQL Tutorial].dbo.EmployeeSalary

--SELECT dem.FirstName, dem.LastName, dem.Gender, sal.Salary,
--	COUNT(Gender) OVER (PARTITION BY Gender) as TotalGender
--FROM [SQL Tutorial].dbo.EmployeeDemographics dem
--JOIN [SQL Tutorial].dbo.EmployeeSalary sal
--	ON dem.EmployeeID = sal.EmployeeID

--SELECT dem.Gender, COUNT(Gender) as ToTalGender
--FROM [SQL Tutorial].dbo.EmployeeDemographics dem
--JOIN [SQL Tutorial].dbo.EmployeeSalary sal
--	ON dem.EmployeeID = sal.EmployeeID
--GROUP BY dem.Gender

--WITH CTE
--WITH SalaryWithAverage AS (
--    SELECT 
--        dem.FirstName,
--        dem.LastName,
--        sal.Salary,
--        AVG(sal.Salary) OVER () AS AvgSalary
--    FROM [SQL Tutorial].dbo.EmployeeDemographics dem
--    JOIN [SQL Tutorial].dbo.EmployeeSalary sal ON dem.EmployeeID = sal.EmployeeID
--)
--SELECT *
--FROM SalaryWithAverage
--WHERE Salary > AvgSalary;


--WITHOUT CTE, Using sub query
--SELECT *
--FROM (
--    SELECT 
--        e.FirstName,
--        s.Salary,
--        AVG(s.Salary) OVER () AS AvgSalary
--    FROM [SQL Tutorial].dbo.EmployeeDemographics e
--    JOIN [SQL Tutorial].dbo.EmployeeSalary s ON e.EmployeeID = s.EmployeeID
--) AS sub
--WHERE Salary > AvgSalary;

--DROP TABLE IF EXISTS #EmployeeTemps;
--CREATE TABLE #EmployeeTemps (
--    EmployeeID INT,
--    Name NVARCHAR(50),
--    Salary INT
--);

--INSERT INTO #EmployeeTemps (EmployeeID, Name, Salary)
--VALUES (101, 'Jim', 60000),
--       (102, 'Pam', 55000);

--SELECT * FROM #EmployeeTemps;

--DROP TABLE IF EXISTS #temp_Employee;
--CREATE TABLE #temp_Employee (
--EmployeeID int,
--JobTitle varchar(100),
--Salary int
--)

--INSERT INTO #temp_Employee
--SELECT *
--FROM [SQL Tutorial].dbo.EmployeeSalary

--SELECT *
--FROM #temp_Employee

--DROP TABLE IF EXISTS #Temp_Employee2
--CREATE TABLE #Temp_Employee2 (
--JobTitle varchar(50),
--EmployeesPerJob int,
--AvgAge int,
--AvgSalary int)

--INSERT INTO #Temp_Employee2
--SELECT JobTitle, Count(JobTitle), Avg(Age), AVG(salary)
--FROM [SQL Tutorial].dbo.EmployeeDemographics emp
--JOIN [SQL Tutorial].dbo.EmployeeSalary sal
--	ON emp.EmployeeID = sal.EmployeeID
--Group By JobTitle

--SELECT *
--FROM #Temp_Employee2

--Drop Table EmployeeErrors;


--CREATE TABLE EmployeeErrors (
--EmployeeID varchar(50)
--,FirstName varchar(50)
--,LastName varchar(50)
--)

--Insert into EmployeeErrors Values 
--('1001  ', 'Jimbo', 'Halbert')
--,('  1002', 'Pamela', 'Beasely')
--,('1005', 'TOby', 'Flenderson - Fired')

--Select *
--From EmployeeErrors

-- Using Trim, LTRIM, RTRIM

--Select EmployeeID, TRIM(employeeID) AS IDTRIM
--FROM EmployeeErrors 

--Select EmployeeID, RTRIM(employeeID) as IDRTRIM
--FROM EmployeeErrors 

--Select EmployeeID, LTRIM(employeeID) as IDLTRIM
--FROM EmployeeErrors 

	

-- Using Replace

--Select LastName, REPLACE(LastName, '- Fired', '') as LastNameFixed
--FROM EmployeeErrors


-- Using Substring

--SELECT *
--FROM EmployeeErrors

--SELECT *
--FROM [SQL Tutorial].dbo.EmployeeDemographics

--Select Substring(err.FirstName,1,3) as 'errFirstName', 
--	   Substring(dem.FirstName,1,3) as 'demFirstName', 
--	   Substring(err.LastName,1,3) as 'errLastName', 
--	   Substring(dem.LastName,1,3) as 'demLastName'
--FROM EmployeeErrors err
--FULL OUTER JOIN [SQL Tutorial].dbo.EmployeeDemographics dem
--	on Substring(err.FirstName,1,3) = Substring(dem.FirstName,1,3) 
--	and Substring(err.LastName,1,3) = Substring(dem.LastName,1,3) 




--SELECT 
--    LastName,
--    SUBSTRING(
--        LastName,3,3
--    ) AS LastName

--FROM [SQL Tutorial].dbo.EmployeeDemographics;




-- Using UPPER and lower

--Select firstname, LOWER(firstname) as 'LoweredFirstName'
--from EmployeeErrors

--Select Firstname, UPPER(FirstName) as 'CapitalizedFirstName'
--from EmployeeErrors



--CREATE PROCEDURE TEST
--AS
--Select *
--From EmployeeDemographics

--EXEC TEST

--CREATE PROCEDURE Temp_Employee
--AS
--BEGIN
--	DROP TABLE IF EXISTS #temp_employee
--	Create table #temp_employee (
--	JobTitle varchar(100),
--	EmployeesPerJob int ,
--	AvgAge int,
--	AvgSalary int
--	)
--	Insert into #temp_employee
--	SELECT JobTitle, Count(JobTitle), Avg(Age), AVG(salary)
--	FROM EmployeeDemographics emp
--	JOIN EmployeeSalary sal
--		ON emp.EmployeeID = sal.EmployeeID
--	group by JobTitle

--	Select * 
--	From #temp_employee
--END;

--GO;

--EXEC Temp_Employee @Jobtitle = 'Salesman'


--AvgAge int,
--AvgSalary int
--)


--Insert into #temp_employee3
--SELECT JobTitle, Count(JobTitle), Avg(Age), AVG(salary)
--FROM SQLTutorial..EmployeeDemographics emp
--JOIN SQLTutorial..EmployeeSalary sal
--	ON emp.EmployeeID = sal.EmployeeID
--where JobTitle = @JobTitle --- make sure to change this in this script from original above
--group by JobTitle

--Select * 
--From #temp_employee3
--GO;


--exec Temp_Employee2 @jobtitle = 'Salesman'
--exec Temp_Employee2 @jobtitle = 'Accountant'

--Select EmployeeID, JobTitle, Salary
--From EmployeeSalary

---- Subquery in Select

--Select EmployeeID, Salary, 
--	(Select AVG(Salary) From EmployeeSalary) as AllAvgSalary
--From EmployeeSalary

---- How to do it with Partition By
--Select EmployeeID, Salary, AVG(Salary) over () as AllAvgSalary
--From EmployeeSalary

---- Why Group By doesn't work
--Select EmployeeID, Salary, AVG(Salary) as AllAvgSalary
--From EmployeeSalary
--Group By EmployeeID, Salary
--order by EmployeeID


-- Subquery in From

--Select a.EmployeeID, AllAvgSalary
--From 
--	(Select EmployeeID, Salary, AVG(Salary) over () as AllAvgSalary
--	 From EmployeeSalary) a
--Order by a.EmployeeID


---- Subquery in Where

--Select EmployeeID, JobTitle, Salary
--From EmployeeSalary
--where EmployeeID in (
--	Select EmployeeID 
--	From EmployeeDemographics
--	where Age > 30)

-- SELECT 
--    country, 
--    date, 
--    total_cases, 
--    total_deaths, 
--    CASE 
--        WHEN CAST(total_cases AS INT) = 0 THEN 0
--        ELSE (CAST(total_deaths AS FLOAT) / CAST(total_cases AS FLOAT)) * 100
--    END AS DeathPercentage
--FROM PortfolioProject.dbo.CovidDeaths
--WHERE country LIKE '%states%'
--ORDER BY country, date;
