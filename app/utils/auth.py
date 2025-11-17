SECRET="CHANGE"
from fastapi.responses import Response
from fastapi import Request
import hashlib,time
def sign(v): return hashlib.sha256((v+SECRET).encode()).hexdigest()
def set_session(r:Response):
 s=str(int(time.time())); r.set_cookie("session",f"{s}:{sign(s)}",httponly=True,samesite="strict")
def check_login(req:Request):
 c=req.cookies.get("session"); 
 if not c: return False
 try: v,s=c.split(":"); return s==sign(v)
 except: return False
def require_login(req): 
 if not check_login(req):
  from fastapi.responses import RedirectResponse
  return RedirectResponse("/",302)
def clear_session(r:Response): r.delete_cookie("session")