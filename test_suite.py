# File to ensure test driven development
import pytest
import duckdb

def test_db_user_data():
    # Pre Set User Inputs
    company = 'VALUE GLOBAL'
    user = 'M.JAMESON'
    cargo = '16X NITROUS OXIDE - 360ML'

    # Connect to Database
    conn = duckdb.connect('database/logger.db')
    pass
