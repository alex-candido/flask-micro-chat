from typing import Optional

from prisma import Prisma, register, get_client
from flask import Flask, render_template, request, flash, redirect, url_for, g

class PrismaModule():
    
    def get_db() -> Prisma:
        try:
            return g.db
        except AttributeError:
            g.db = db = Prisma()
            db.connect()
            return db


    def close_db(exc: Optional[Exception] = None) -> None:  # noqa: ARG001
        client = get_client()
        if client.is_connected():
            client.disconnect()
        
