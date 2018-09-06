import pymysql.cursors
import settings


conn = pymysql.connect( 
    host=settings.ddbb_host, port=3306,
    user=settings.ddbb_user,passwd =settings.ddbb_pw, db='expenses',
    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor,
    local_infile=True)

create_expenses_table_statement = """ 
        CREATE TABLE expenses.expenses (
        id int(11) NOT NULL AUTO_INCREMENT,
        who varchar(255) NOT NULL,
        topic varchar(255) NOT NULL,
        subtopic varchar(255) NOT NULL,
        month varchar(255) NOT NULL,  
        month_day int(4),
        week_day varchar(255), 
        expense float(7,2) NOT NULL,
        comment varchar(255) NOT NULL,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 
        AUTO_INCREMENT=1 ;
    """
def create_expenses_table():
    execute(create_expenses_table_statement)

def insert_row_query_stament(row):
    return """  INSERT INTO `expenses` (`who`, `topic`, `subtopic`, `month`, `month_day`, `week_day`, `expense`, `comment`) 
                VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", {6}, "{7}")
            """.format(row['quien'], row['tipo'], row['subtipo'], row['mes'], 
                    row['dia_mes'], row['dia_semana'], row['gasto'], row['comentario'])

def insert_expense(row):
    execute(insert_row_query_stament(row))

def execute(stament):
    print(stament)
    conn.cursor().execute(stament)
    conn.commit()
    

