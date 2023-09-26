import streamlit as st
import pandas as pd

# Data storage (using pandas DataFrame for simplicity)
products = pd.DataFrame(columns=["ID", "Name", "Quantity"])
requests = pd.DataFrame(columns=["ID", "Project Name", "Project Number", "Desired Delivery Date", "Products", "Quantities"])
invoices = pd.DataFrame(columns=["ID", "Type", "Date", "Products", "Quantities"])

def app():
    st.title("Складской учет")
    
    # Menu
    menu = ["Главная", "Добавить товар", "Создать заявку", "Создать накладную"]
    choice = st.sidebar.selectbox("Меню", menu)
    
    if choice == "Главная":
        st.subheader("Текущий список товаров на складе:")
        st.write(products)
        
    elif choice == "Добавить товар":
        st.subheader("Добавить новый товар")
        product_data = st.beta_expander("Добавить товар в таблицу", False)
        with product_data:
            product_id = st.number_input("ID", value=products.shape[0] + 1)
            product_name = st.text_input("Наименование товара")
            product_quantity = st.number_input("Количество", value=0)
            if st.button("Добавить товар"):
                products.loc[product_id] = [product_id, product_name, product_quantity]
                st.success(f"Товар {product_name} добавлен!")
            
    elif choice == "Создать заявку":
        st.subheader("Создать новую заявку")
        request_data = st.beta_expander("Добавить заявку в таблицу", False)
        with request_data:
            #... (similar approach as adding product)
            
    elif choice == "Создать накладную":
        st.subheader("Создать новую накладную")
        invoice_data = st.beta_expander("Добавить накладную в таблицу", False)
        with invoice_data:
            #... (similar approach as adding product and request)

if __name__ == "__main__":
    app()
