## Natural Join and Equi Join

- both works the same way as inner join

- Natural Join

  - No condition need to be give on joining
  - Column Name should be same between the two tables to let know sql which columns to join
  - Not available in mssql
  - Basic syntax :

  ```sql
    select * from employee natural join department
  ```

- Equi Join

  - Condition should be specified
  - Condition should always be about equality,
    it should always use '=' while joinning

## Declare Variables

```sql
    declare @d Date = GETDATE();
    select format(@d,'dd/MM/yyyy','en-US') as 'Date';
```
