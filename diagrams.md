# ATM Machine Simulation System – Diagrams

This file contains the design diagrams for the ATM Machine Simulation System.

## 1. System Architecture

```mermaid
flowchart TD
    U[User] --> M[main.py]

    M --> AUTH[authentication.py]
    M --> ATM[atm.py]
    M --> ACC[account.py]

    ATM --> TRANS[transactions.py]
    ATM --> HIST[transaction_history.py]
    ATM --> ACC

    AUTH --> DB[database.py]
    ACC --> DB
    TRANS --> DB
    HIST --> DB

    ACC --> VAL[validation.py]
    TRANS --> VAL

flowchart TD
    S([Start]) --> O[Open ATM System]
    O --> MM[Main Menu]

    MM --> L[Login]
    MM --> C[Create New Account]
    MM --> E[Exit]

    C --> MM
    E --> END([End])

    L --> INPUT[Enter Account Number and PIN]
    INPUT --> CHECK{Authentication Check}

    CHECK -->|Invalid| ERROR[Show Error Message]
    ERROR --> L

    CHECK -->|Valid| ATM[ATM Menu]

    ATM --> CHOICE{Select Operation}

    CHOICE --> B[Check Balance]
    CHOICE --> D[Deposit Money]
    CHOICE --> W[Withdraw Money]
    CHOICE --> T[Transfer Money]
    CHOICE --> A[Account Details]
    CHOICE --> H[Transaction History]
    CHOICE --> P[Change PIN]
    CHOICE --> LOGOUT[Logout]

    B --> ATM
    D --> ATM
    W --> ATM
    T --> ATM
    A --> ATM
    H --> ATM
    P --> ATM

    LOGOUT --> MM


flowchart LR
    U[User]

    subgraph ATM[ATM Machine Simulation System]
        L[Login]
        C[Create Account]
        B[Check Balance]
        D[Deposit Money]
        W[Withdraw Money]
        T[Transfer Money]
        A[View Account Details]
        H[View Transaction History]
        P[Change PIN]
        O[Logout]
    end

    U --- L
    U --- C
    U --- B
    U --- D
    U --- W
    U --- T
    U --- A
    U --- H
    U --- P
    U --- O


classDiagram

class Main {
    +main()
}

class Authentication {
    +login()
}

class ATM {
    +atm_menu()
}

class Account {
    +create_account()
    +get_account_details()
    +change_pin()
}

class Transactions {
    +check_balance()
    +deposit()
    +withdraw()
    +transfer()
}

class TransactionHistory {
    +add_transaction()
    +show_history()
}

class Validation {
    +validate_amount()
    +validate_pin()
    +validate_account_number()
}

class Database {
    +accounts
}

Main --> Authentication
Main --> ATM
Main --> Account

Authentication --> Database
ATM --> Transactions
ATM --> Account
ATM --> TransactionHistory

Account --> Validation
Transactions --> Validation

Account --> Database
Transactions --> Database
TransactionHistory --> Database


sequenceDiagram
    actor User
    participant Main as main.py
    participant Auth as authentication.py
    participant ATM as atm.py
    participant Trans as transactions.py
    participant DB as database.py

    User->>Main: Select Login
    Main->>Auth: login()
    Auth->>User: Enter account number and PIN
    User-->>Auth: Account number + PIN

    Auth->>DB: Check account and PIN
    DB-->>Auth: Authentication result

    alt Valid credentials
        Auth-->>Main: Login successful
        Main->>ATM: Open ATM menu

        ATM->>User: Display ATM menu
        User->>ATM: Select transaction

        ATM->>Trans: Perform transaction
        Trans->>DB: Read/update account data
        DB-->>Trans: Updated data

        Trans-->>ATM: Transaction result
        ATM-->>User: Display result

    else Invalid credentials
        Auth-->>User: Invalid account number or PIN
    end


flowchart TD
    DB[database.py]

    DB --> ACC[accounts dictionary]

    ACC --> NUM[Account Number]
    NUM --> NAME[Name]
    NUM --> PIN[PIN]
    NUM --> BAL[Balance]
    NUM --> HIST[Transactions List]

    HIST --> D[Deposit]
    HIST --> W[Withdrawal]
    HIST --> T[Transfer]


flowchart TD
    MAIN[main.py]

    MAIN --> AUTH[authentication.py]
    MAIN --> ATM[atm.py]
    MAIN --> ACCOUNT[account.py]

    ATM --> TRANS[transactions.py]
    ATM --> HISTORY[transaction_history.py]
    ATM --> ACCOUNT

    AUTH --> DATABASE[database.py]
    ACCOUNT --> DATABASE
    TRANS --> DATABASE
    HISTORY --> DATABASE

    ACCOUNT --> VALIDATION[validation.py]
    TRANS --> VALIDATION