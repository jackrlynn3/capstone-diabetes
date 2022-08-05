-- Make sure in the right database
USING group5database;
GO

-- Drop exisiting versions of the database
DROP TABLE IF EXISTS CensusStat;
DROP TABLE IF EXISTS [State];
DROP TABLE IF EXISTS Metric;
DROP TABLE IF EXISTS GlucoseMeter;
DROP TABLE IF EXISTS DiabetesPop;
DROP TABLE IF EXISTS Demographic;
GO

-- Create demographic table
CREATE TABLE Demographic (
    demoID INT PRIMARY KEY NOT NULL, -- PK
    demo_group VARCHAR(30) NOT NULL,
    category VARCHAR(15) NOT NULL,
    CONSTRAINT u_demo_group_category -- Uniqueness of demographic
        UNIQUE (demo_group, category)
);

-- Create Chinese diabetes population table
CREATE TABLE DiabetesPop (
    personID INT PRIMARY KEY NOT NULL, -- PK
    age INT NOT NULL,
    sexID INT NOT NULL, -- FK
    height DECIMAL(4, 1) NOT NULL,
    [weight] DECIMAL(4, 1) NOT NULL,
    bmi DECIMAL(3, 1) NOT NULL,
    sbp INT NOT NULL,
    dbp INT NOT NULL,
    fgp DECIMAL(4, 2) NOT NULL,
    chol DECIMAL(4, 2) NOT NULL,
    tg DECIMAL(4, 2) NOT NULL,
    hdlc DECIMAL(5, 3) NOT NULL,
    ldl DECIMAL(5, 3) NOT NULL,
    alt DECIMAL(4, 2) NOT NULL,
    ast DECIMAL(5, 3) NOT NULL,
    bun DECIMAL(4, 2) NOT NULL,
    ccr DECIMAL(4, 2) NOT NULL,
    fgp_final DECIMAL(4, 2) NOT NULL,
    diabetes BINARY NOT NULL,
    smokerID INT NOT NULL,
    drinkerID INT NOT NULL,
    famhistID INT NOT NULL,
    CONSTRAINT u_personID
        UNIQUE (personID),
);

-- Create GlucoseMeter table
CREATE TABLE GlucoseMeter (
    recID INT PRIMARY KEY NOT NULL, -- PK
    [time] VARCHAR(30) NOT NULL,
    glucose_lvl INT NOT NULL,
    ptID INT NOT NULL, -- FK
    CONSTRAINT u_recID
        UNIQUE(recID)
);

-- Create State table

CREATE TABLE [State] (
    stateID varchar(2) PRIMARY KEY NOT NULL, -- PK
    [name] varchar(20) NOT NULL,
    CONSTRAINT u_stateID
        UNIQUE (stateID)
);

-- Create Metric table

CREATE TABLE [Metric] (
    metricID INT PRIMARY KEY NOT NULL, -- PK
    metric VARCHAR(30) NOT NULL,
    unit VARCHAR(10) NULL,
    CONSTRAINT u_metricID
        UNIQUE (metricID),
    CONSTRAINT u_metric
        UNIQUE (metric)
);

-- Create CensusStat table

CREATE TABLE CensusStat (
    stateID varchar(2) NOT NULL, -- PK
    metricID INT NOT NULL, -- PK
    demoID INT NOT NULL, -- PK
    [year] INT NOT NULL,
    [value] DECIMAL(5, 2)
);