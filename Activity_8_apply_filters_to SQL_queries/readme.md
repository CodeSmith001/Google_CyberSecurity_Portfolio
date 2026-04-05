# Portfolio Activity: Apply Filters to SQL Queries

## 📝 Objective
The objective of this project was to utilize Structured Query Language (SQL) to investigate potential security incidents and assist with IT asset management. This involved writing robust `SELECT` queries to extract actionable data from relational databases, specifically focusing on the `log_in_attempts` and `employees` tables.

## 🛠️ Skills Demonstrated
- Database Querying & Log Analysis
- **SQL Data Manipulation Language (DML):** `SELECT`, `FROM`, `WHERE`
- **SQL Logical Operators:** `AND`, `OR`, `NOT`
- **SQL Pattern Matching:** `LIKE`, `%` wildcard
- Filtering by Date, Time, and Text Strings

## 🏢 Scenario: Security Investigation and System Updates
**Situation:** 
As a security professional at a large organization, I was tasked with investigating a series of suspicious login attempts, including after-hours access and international login discrepancies. Concurrently, the IT department required specific lists of employee machines designated for targeted security patching.

**Task:** 
My task was to examine the organization’s databases and craft precise SQL filters to retrieve the necessary records. I needed to identify failed after-hours logins, isolate login activity on specific dates, exclude logins from specific countries (accounting for inconsistent data entry), and segment employees by department and physical office location.

## 🚀 Action Taken
To retrieve the required information, I executed a series of SQL queries utilizing various filtering techniques:
1. **Time and Status Filtering:** Used `WHERE login_time > '18:00:00' AND success = 0` to identify failed after-hours login attempts.
2. **Date Filtering:** Used the `OR` operator to isolate activity to a specific 48-hour window (`login_date = '2022-05-08' OR login_date = '2022-05-09'`).
3. **Pattern Matching & Exclusion:** Utilized `WHERE NOT country LIKE 'MEX%'` to filter out logins from Mexico. The `%` wildcard was crucial here to account for inconsistent data entry (capturing both 'MEX' and 'MEXICO').
4. **Multi-Condition Filtering:** Combined `AND` and `LIKE` operators to find specific targets for security updates (e.g., `department = 'Marketing' AND office LIKE 'East%'`).
5. **Departmental Exclusion:** Used the `NOT` operator to exclude employees who had already received security updates (`NOT department = 'Information Technology'`).

## 📈 Results
The SQL queries successfully extracted the precise datasets required by the security and IT teams. By leveraging logical operators and wildcards, I ensured the retrieved data was clean and accurate, allowing the security team to proceed with their incident investigation and the IT team to deploy their targeted security patches efficiently.

## 📁 Files Included
*   `[Apply filters to SQL queries.pdf]` - Detailed report containing the SQL queries, explanations of the logic used, and annotated screenshots of the database outputs.
