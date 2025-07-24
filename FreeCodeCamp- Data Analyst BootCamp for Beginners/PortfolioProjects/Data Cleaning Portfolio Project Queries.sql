/*

Cleaning Data in SQL Queries

*/


Select *
From PortfolioProject.dbo.NashvilleHousing
Where OwnerName is NOT NULL
Order By OwnerNAme

--------------------------------------------------------------------------------------------------------------------------

-- Standardize Date Format
Select SaleDate
From PortfolioProject.dbo.NashvilleHousing

Select SaleDate, CONVERT(datetime2,SaleDate)
From PortfolioProject.dbo.NashvilleHousing

Update NashvilleHousing
SET SaleDate = CONVERT(datetime2,SaleDate)


ALTER TABLE NashvilleHousing
DROP COLUMN SaleDateConverted

-- If it doesn't Update properly

--Adding new columnn
ALTER TABLE NashvilleHousing
Add SaleDateConverted datetime2;

Update NashvilleHousing
SET SaleDateConverted = CONVERT(datetime2,SaleDate)


 --------------------------------------------------------------------------------------------------------------------------

--POPULATE PROPERTY ADDRESS DATA

--Confirmig duplicate PArcelID and PropertyAddress
SELECT ParcelID,PropertyAddress, COUNT(*) as count
FROM NashvilleHousing
GROUP BY ParcelID, PropertyAddress
HAVING COUNT(*) > 1;

--Display each row of duplicates
SELECT ParcelID, PropertyAddress, OwnerName, OwnerAddress, TaxDistrict, YearBuilt,
       COUNT(*) OVER (PARTITION BY OwnerName) AS duplicate_count
FROM NashvilleHousing
Where OwnerName is NOT NULL AND PropertyAddress is NULL
ORDER BY OwnerName;

--Display NULL column in relation to OwnerNames that has duplicates
SELECT ParcelID, PropertyAddress, OwnerName, 
	   OwnerAddress, TaxDistrict, YearBuilt
FROM NashvilleHousing
WHERE OwnerName IN (
    SELECT OwnerName
    FROM NashvilleHousing
    WHERE PropertyAddress IS NULL
    GROUP BY OwnerName
    HAVING COUNT(*) >= 1
)
AND OwnerName IS NOT NULL
ORDER BY OwnerName;




Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress,b.PropertyAddress)
From PortfolioProject.dbo.NashvilleHousing a
JOIN PortfolioProject.dbo.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID] <> b.[UniqueID]
Where a.PropertyAddress is null


Update a
SET PropertyAddress = ISNULL(a.PropertyAddress,b.PropertyAddress)
From PortfolioProject.dbo.NashvilleHousing a
JOIN PortfolioProject.dbo.NashvilleHousing b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID] <> b.[UniqueID]
Where a.PropertyAddress is null




--------------------------------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)


Select PropertyAddress
From PortfolioProject.dbo.NashvilleHousing
--Where PropertyAddress is null
--order by ParcelID


SELECT
 --first letter (1) upto before comma, -1 makes it to not include comma
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 ) as Address1

-- from comma (+1 makes comma not included) up to the last letter (LEN) 
,SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress)) as Address2

From PortfolioProject.dbo.NashvilleHousing

--Create new column for address
ALTER TABLE NashvilleHousing
Add PropertySplitAddress Nvarchar(255);

Update NashvilleHousing
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 )

--Create new column for city
ALTER TABLE NashvilleHousing
Add PropertySplitCity Nvarchar(255);

Update NashvilleHousing
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))




Select *
From PortfolioProject.dbo.NashvilleHousing





Select OwnerAddress
From PortfolioProject.dbo.NashvilleHousing


Select
PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)
From PortfolioProject.dbo.NashvilleHousing



ALTER TABLE NashvilleHousing
Add OwnerSplitAddress Nvarchar(255);

ALTER TABLE NashvilleHousing
Add OwnerSplitCity Nvarchar(255);

ALTER TABLE NashvilleHousing
Add OwnerSplitState Nvarchar(255);



Update NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)

Update NashvilleHousing
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)

Update NashvilleHousing
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)


Select *
From PortfolioProject.dbo.NashvilleHousing




--------------------------------------------------------------------------------------------------------------------------


-- Change Y and N to Yes and No in "Sold as Vacant" field


Select Distinct(SoldAsVacant), Count(SoldAsVacant)
From PortfolioProject.dbo.NashvilleHousing
Group by SoldAsVacant
order by 2




Select SoldAsVacant
, CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END
From PortfolioProject.dbo.NashvilleHousing


Update NashvilleHousing
SET SoldAsVacant = CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END






-----------------------------------------------------------------------------------------------------------------------------------------------------------

-- Remove Duplicates
WITH RowNumCTE AS 
(    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY ParcelID,PropertyAddress,
                     SalePrice,SaleDate,LegalReference
            ORDER BY UniqueID
        ) AS row_num
    FROM PortfolioProject.dbo.NashvilleHousing
)


SELECT ParcelID,PropertyAddress,SalePrice,
    SaleDate, LegalReference,UniqueID,row_num,
    CASE -- case statement just to clearly see the duplicate
        WHEN row_num > 1 THEN 'Duplicate'
        ELSE 'Original'
    END AS RecordStatus
FROM RowNumCTE
WHERE row_num > 1  -- Uncomment to see only duplicates
ORDER BY ParcelID,PropertyAddress,SaleDate, row_num;

--Deleteing duplicates 
--DELETE
--FROM RowNumCTE
--WHERE row_num > 1



Select *
From PortfolioProject.dbo.NashvilleHousing




---------------------------------------------------------------------------------------------------------

-- Delete Unused Columns

Select *
From PortfolioProject.dbo.NashvilleHousing
    
ALTER TABLE PortfolioProject.dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDateConverted















-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------

--- Importing Data using OPENROWSET and BULK INSERT	

--  More advanced and looks cooler, but have to configure server appropriately to do correctly
--  Wanted to provide this in case you wanted to try it


--sp_configure 'show advanced options', 1;
--RECONFIGURE;
--GO
--sp_configure 'Ad Hoc Distributed Queries', 1;
--RECONFIGURE;
--GO


--USE PortfolioProject 

--GO 

--EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1 

--GO 

--EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DynamicParameters', 1 

--GO 


---- Using BULK INSERT

--USE PortfolioProject;
--GO
--BULK INSERT nashvilleHousing FROM 'C:\Temp\SQL Server Management Studio\Nashville Housing Data for Data Cleaning Project.csv'
--   WITH (
--      FIELDTERMINATOR = ',',
--      ROWTERMINATOR = '\n'
--);
--GO


---- Using OPENROWSET
--USE PortfolioProject;
--GO
--SELECT * INTO nashvilleHousing
--FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0',
--    'Excel 12.0; Database=C:\Users\alexf\OneDrive\Documents\SQL Server Management Studio\Nashville Housing Data for Data Cleaning Project.csv', [Sheet1$]);
--GO


















