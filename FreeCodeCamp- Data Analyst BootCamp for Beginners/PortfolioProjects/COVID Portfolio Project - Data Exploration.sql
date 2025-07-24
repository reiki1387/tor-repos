/*
Covid 19 Data Exploration 

Skills used: Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types

*/

Select *
From PortfolioProject..CovidDeaths
Where continent is not null 
order by 3,4


-- Select Data that we are going to be starting with

Select country, date, total_cases, new_cases, total_deaths, population
From PortfolioProject..CovidDeaths
Where continent is not null 
order by 1,2


-- Total Cases vs Total Deaths (Avoiding Divide by zero using NULLIF)
-- Shows likelihood of dying if you contract covid in your country

Select country, date, total_cases,total_deaths, 
	  (total_deaths/NULLIF(total_cases, 0))*100 as DeathPercentage
From PortfolioProject..CovidDeaths
Where country like '%states%'
and continent is not null 
order by 1,2


--Total Cases vs Total Deaths \
--(Avoiding Divide by zero using CASE Statemetn)
SELECT country,date,total_cases, total_deaths, 
    CASE 
        WHEN total_cases = 0 THEN NULL
        ELSE (total_deaths / total_cases) * 100
    END AS DeathPercentage
FROM 
    PortfolioProject..CovidDeaths
WHERE 
    country LIKE '%states%'
    AND continent IS NOT NULL
ORDER BY 
    country, date;




-- Total Cases vs Population
-- Shows what percentage of population infected with Covid

Select country, date, Population, total_cases,  (total_cases/population)*100 as PercentPopulationInfected
From PortfolioProject..CovidDeaths
--Where location like '%states%'
order by 1,2


-- Countries with Highest Infection Rate compared to Population

Select country, Population, MAX(total_cases) as HighestInfectionCount,  
		MAX(cast(total_cases as int)) / cast (population as int) *100  as PercentPopulationInfected --always zero
		--MAX((total_cases / CAST(Population AS FLOAT))) * 100 as PercentPopulationInfected
From PortfolioProject..CovidDeaths
Where continent is not null 
--Where location like '%states%'
Group by country, Population
order by PercentPopulationInfected desc


-- Countries with Highest Death Count per Population

Select country, MAX(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths
--Where location like '%states%'
Where continent is not null 
Group by country
order by TotalDeathCount desc



-- BREAKING THINGS DOWN BY CONTINENT

-- Showing contintents with the highest death count per population

Select continent, MAX(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths
--Where continent is not null 
Group by continent
order by TotalDeathCount desc



-- GLOBAL NUMBERS

Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, 
		SUM(cast(new_deaths as float))/SUM(New_Cases)*100 as DeathPercentage
From PortfolioProject..CovidDeaths
--Where location like '%states%'
where continent is not null 
--Group By date
order by 1,2



-- Total Population vs Vaccinations
-- Shows Percentage of Population that has recieved at least one Covid Vaccine

SELECT 
    dea.continent, 
    dea.country, 
    dea.date, 
    dea.population, 
    vac.new_vaccinations,
    SUM(vac.new_vaccinations)
        OVER (
            PARTITION BY dea.country 
            ORDER BY CONVERT(VARCHAR(255), dea.country), dea.date
            ) AS RollingPeopleVaccinated
   -- ,(RollingPeopleVaccinated/population)*100 -- derived column cannot be usein the same select clause
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
    ON dea.country = vac.country
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY dea.country, dea.date;



--checking if there are more than
--1 row per country per day

SELECT 
    dea.country,
    dea.date,
    COUNT(*) AS NumRows
FROM 
    PortfolioProject..CovidDeaths dea
JOIN 
    PortfolioProject..CovidVaccinations vac
    ON dea.country = vac.country AND dea.date = vac.date
WHERE 
    dea.continent IS NOT NULL
GROUP BY 
    dea.country, dea.date
HAVING 
    COUNT(*) > 1
ORDER BY 
    NumRows DESC;


--Checking if the new_vaccinations are cumulative or
--reseting 
    SELECT 
    country, 
    date, 
    new_vaccinations
FROM 
    PortfolioProject..CovidVaccinations
WHERE 
    country = 'United States' -- or any country
ORDER BY 
    date;







-- Using CTE to perform Calculation on Partition By in previous query

With PopvsVac (Continent, Country, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as 
(
    SELECT 
        dea.continent, 
        dea.country, 
        dea.date, 
        dea.population, 
        vac.new_vaccinations,
        SUM(vac.new_vaccinations) 
            OVER (
                PARTITION BY dea.country 
                ORDER BY CONVERT(VARCHAR(255), dea.country), dea.date
                 ) AS RollingPeopleVaccinated
    FROM  PortfolioProject..CovidDeaths dea
    JOIN PortfolioProject..CovidVaccinations vac
        ON dea.country = vac.country 
        AND dea.date = vac.date
    WHERE dea.continent IS NOT NULL
)
SELECT *, (CAST(RollingPeopleVaccinated AS FLOAT)/Population)*100 
            AS PercentPopulationVaccinated
FROM PopvsVac;






-- Using Temp Table to perform Calculation on Partition By in previous query

DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Country nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
Select dea.continent, dea.country, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (
        Partition by dea.country 
        Order by CONVERT(VARCHAR(255), dea.country), dea.Date
        ) as RollingPeopleVaccinated

From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
	On dea.country = vac.country
	and dea.date = vac.date
where dea.continent is not null 
order by 2,3

Select *, (CAST(RollingPeopleVaccinated AS FLOAT)/Population)*100 
            AS PercentPopulationVaccinated
From #PercentPopulationVaccinated




-- Creating View to store data for later visualization
Create View PercentPopulationVaccinated 
as
Select dea.continent, dea.country, dea.date, dea.population, vac.new_vaccinations
, SUM(vac.new_vaccinations) OVER (
        Partition by dea.country 
        Order by  CONVERT(VARCHAR(255), dea.country), dea.Date
        ) as RollingPeopleVaccinated

From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
	On dea.country = vac.country
	and dea.date = vac.date
where dea.continent is not null 


