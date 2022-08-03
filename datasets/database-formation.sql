-- Make sure in the right database
USING group5database;
GO

-- Drop exisiting versions of the database
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
    CONSTRAINT fk_sexID_Demographic
        FOREIGN KEY (sexID)
        REFERENCES Demographic(demoID),
    CONSTRAINT fk_smokerID_Demographic
        FOREIGN KEY (smokerID)
        REFERENCES Demographic(demoID),
    CONSTRAINT fk_drinkerID_Demographic
        FOREIGN KEY (drinkerID)
        REFERENCES Demographic(demoID),
    CONSTRAINT fk_famhistID_Demographic
        FOREIGN KEY (famhistID)
        REFERENCES Demographic(demoID)
);