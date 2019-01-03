gosu postgres psql --dbname template1 <<EOSQL
    CREATE EXTENSION hstore;
    DROP DATABASE $POSTGRES_DB;
    CREATE DATABASE $POSTGRES_DB TEMPLATE template1;
EOSQL