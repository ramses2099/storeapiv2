from typing import List, Optional, Union, Any
from datetime import datetime
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    SecretStr,
    ValidationError,)
 
class User(BaseModel):
    id: int
    username: str 
    email: EmailStr 
    firstname:str
    lastname: str    
    updated: Optional[datetime] = None
    created: Optional[datetime] = None 
       
class UserUpdate(BaseModel):
    id: int
    username: str
    password: str
    email: str
    firstname:str
    lastname: str    
    updated: Optional[datetime] = datetime.now() 
    
class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    firstname:str
    lastname: str
    created: Optional[datetime] = datetime.now()    
    
class Customer(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    updated: Optional[datetime] = None
    created: Optional[datetime] = None 
    
class CustomerUpdate(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    updated: Optional[datetime] = datetime.now()    
    
class CustomerCreate(BaseModel):
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    created: Optional[datetime] = datetime.now()
    
class Order(BaseModel):
    id: int
    orderdate: datetime
    shipdate: datetime
    ordertotal: float
    
    # relationship here
    customer_id: int
    employee_id: int  
    user_id: int 
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = None 
    
class OrderUpdate(BaseModel):
    id: int
    orderdate: datetime
    shipdate: datetime
    ordertotal: float
    
    # relationship here
    customer_id: int
    employee_id: int  
    user_id: int 
    updated: Optional[datetime] = datetime.now()
    
class OrderCreate(BaseModel):
    orderdate: datetime
    shipdate: datetime
    ordertotal: float
    
    # relationship here
    customer_id: int
    employee_id: int  
    user_id: int 
    
    # order and order details
    ordersdetails: Optional[List["Order_Detail"]] = []
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = datetime.now() 


class Order_Detail(BaseModel):
    id: int
    price: float
    quantity: int
    
    # relationship here
    order_id: int
    product_id: int
    user_id: int
    
    updated:Optional[datetime] = None
    created:Optional[datetime] = None
    
    
class Order_DetailUpdate(BaseModel):
    id: int
    price: float
    quantity: int
    
    # relationship here
    order_id: int
    product_id: int
    user_id: int
    
    updated:Optional[datetime] = datetime.now()
    
class Order_DetailCreate(BaseModel):
    price: float
    quantity: int
    
    # relationship here
    order_id: int
    product_id: int
    user_id: int
    
    updated:Optional[datetime] = None
    created:Optional[datetime] = datetime.now()
    
class Product(BaseModel):
    id: int
    name: str
    description: str
    priceperunit: float
    quantityonhand: int
   
    # relationship here
    category_id: int
    user_id: int
      
    updated:Optional[datetime] = None
    created:Optional[datetime] = None
    
class ProductUpdate(BaseModel):
    id: int
    name: str
    description: str
    priceperunit: float
    quantityonhand: int
   
    # relationship here
    category_id: int
    user_id: int
      
    updated:Optional[datetime] = datetime.now()
    
class ProductCreate(BaseModel):
    name: str
    description: str
    priceperunit: float
    quantityonhand: int
   
    # relationship here
    category_id: int
    user_id: int
      
    updated:Optional[datetime] = None
    created:Optional[datetime] = datetime.now()
    
class Employee(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    dbo: datetime
    user_id: int
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = None 
    
    
class EmployeeUpdate(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    dbo: datetime
    user_id: int
    
    updated: Optional[datetime] = datetime.now()
    
class EmployeeCreate(BaseModel):
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    dbo: datetime
    user_id: int
    created: Optional[datetime] = datetime.now()
    
class Category(BaseModel):
    id: int
    description: str
    user_id: int
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = None
    
class CategoryUpdate(BaseModel):
    id: int
    description: str
    user_id: int
    
    updated: Optional[datetime] = datetime.now()
    
    
class CategoryCreate(BaseModel):
    description: str
    user_id: int
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = datetime.now()
  
  
class Vendor(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    user_id: int
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = None 
    
class VendorUpdate(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    user_id: int
    
    updated: Optional[datetime] = datetime.now()
    
    
class VendorCreate(BaseModel):
    id: int
    firstname: str
    lastname: str
    streetaddress: str
    city: str
    state: str
    zipcode: str
    phonenumber: str
    email: str
    user_id: int
    
    updated: Optional[datetime] = None
    created: Optional[datetime] = datetime.now()