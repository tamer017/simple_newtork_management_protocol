# simple_newtork_management_protocol

A user-friendly graphical interface for streamlined SNMP network management and operational logging.

## Overview

The `simple_newtork_management_protocol` project provides a straightforward graphical user interface (GUI) for interacting with SNMP (Simple Network Management Protocol) agents. It simplifies the process of performing fundamental SNMP operations, enabling users to retrieve (GET, GETNEXT) and modify (SET) Management Information Base (MIB) variables on network devices.

This application addresses the need for a quick, visual tool to execute manual SNMP commands without resorting to complex command-line utilities or scripting. It enhances operational transparency by automatically logging all SNMP interactions, including details such as agent IP, manager IP, action performed, OID, and operation output, to a local CSV file.

The tool is designed for network administrators, developers, and IT professionals who require an intuitive interface for ad-hoc SNMP queries, configuration changes, and a persistent record of these operations for auditing or troubleshooting purposes.

## Architecture

The application employs a monolithic architecture, centered around a Tkinter-based graphical user interface.

-   **GUI (`app.py`)**: Serves as the primary entry point and user interface, managing user inputs for SNMP parameters and displaying operation results. It orchestrates calls to the backend modules.
-   **SNMP Module (`SNMP.py`)**: Encapsulates the core logic for SNMP communication. It provides functions to execute standard SNMPv2c GET, GETNEXT, and SET operations against specified network agents using the `pysnmp` library.
-   **Logging Module (`logs.py`)**: Responsible for persistent data recording. This module handles the structured logging of every SNMP operation, including timestamps and operational details, to a local `logs.csv` file.

## Key Features

-   **Basic SNMP Operations**: Supports standard SNMPv2c GET, GETNEXT, and SET operations for interacting with network devices.
-   **Intuitive Graphical User Interface**: Provides a user-friendly Tkinter-based interface for easy input of SNMP parameters and display of results.
-   **Comprehensive Operational Logging**: Automatically logs all SNMP interactions, including agent IP, manager IP, action, OID, value (for SET operations), and output, to a local CSV file for auditing and record-keeping.

## Technologies

-   **Python**: The primary programming language used for the entire application.
-   **Tkinter**: Python's standard GUI toolkit, utilized for building the graphical user interface.
-   **pysnmp**: A pure-Python SNMP library, providing the core functionality for SNMP communication.
-   **socket**: Python's low-level networking interface, used for retrieving manager network information.
-   **datetime**: Python's standard library for timestamping log entries.
-   **csv**: Python's standard library for reading and writing CSV files, used for operational logging.

## Getting Started

To set up and run the `simple_newtork_management_protocol` application, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/simple_newtork_management_protocol.git
    cd simple_newtork_management_protocol
    ```

2.  **Install dependencies:**
    The project requires the `pysnmp` library. It is recommended to use a virtual environment.
    ```bash
    pip install pysnmp
    ```

3.  **Run the application:**
    Execute the main application script:
    ```bash
    python app.py
    ```
    This will launch the graphical user interface, allowing interaction with SNMP agents. Operational logs will be recorded in `logs.csv` in the project root directory.