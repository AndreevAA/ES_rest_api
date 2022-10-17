import psycopg2
from flask import Blueprint, render_template, redirect, url_for, request


# Объект связки БД
from psycopg2._psycopg import AsIs


class DB:

    # Поле соединение с БД
    conn = None

    def __init__(self):
        self.open_conn()

    def open_conn(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="ES",
            user='postgres',
            password='qwerty')

    def get_id_for_new_user(self):
        return self.get_max_user_id() + 1

    def get_max_user_id(self):
        self.open_conn()
        cur_t = self.conn.cursor()
        cur_t.execute('select max_id() from inner_s.users')
        f_usr = cur_t.fetchall()
        usr_id = f_usr[0][0]
        cur_t.close()
        return usr_id

    def cnt_user_login(self, new_user_login):
        self.open_conn()
        cur_t = self.conn.cursor()
        print(new_user_login)
        cur_t.execute(
            'select count(*) from inner_s.users where login = (%s)',
            (new_user_login,)
        )
        f_usr = cur_t.fetchall()
        print(f_usr)
        usr_login_cnt = f_usr[0][0]
        cur_t.close()
        print("usr_login_cnt", usr_login_cnt)
        return usr_login_cnt

    def is_user_login_existed(self, new_user_login):
        if self.cnt_user_login(new_user_login) > 0:
            return True
        return False

    def get_id_for_new_passport(self):
        return self.get_max_passport_id() + 1

    def get_max_passport_id(self):
        self.open_conn()
        cur_t = self.conn.cursor()
        cur_t.execute("select MAX('passport_id') from w_dir.passports")
        f_usr = cur_t.fetchall()
        psprt_id = f_usr[0][0]
        cur_t.close()
        return psprt_id

