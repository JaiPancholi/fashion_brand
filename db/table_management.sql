CREATE TABLE fashion_product_page 
  ( 
     id               BIGSERIAL, 
     brand_name       TEXT, 
     gender           TEXT, 
     category_url     TEXT, 
     product_page_url TEXT PRIMARY KEY, 
     created_at       TIMESTAMP DEFAULT Now(), 
     updated_at       TIMESTAMP DEFAULT Now() 
  ); 

CREATE TABLE fashion_image_links 
  ( 
     id               BIGSERIAL, 
     brand_name       TEXT, 
     gender           TEXT, 
     product_page_url TEXT REFERENCES fashion_product_page (product_page_url), 
     image_url        TEXT PRIMARY KEY, 
     image_name       TEXT, 
     created_at       TIMESTAMP DEFAULT Now(), 
     updated_at       TIMESTAMP DEFAULT Now() 
  ); 