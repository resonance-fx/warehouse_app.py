import streamlit as st

# Sample data structures
products = []
requests = []
invoices = []

# Streamlit app
def app():
    st.title("Складской учет")
    
    # Menu
    menu = ["Главная", "Добавить товар", "Создать заявку", "Создать накладную"]
    choice = st.sidebar.selectbox("Меню", menu)
    
    if choice == "Главная":
        st.subheader("Текущий список товаров на складе:")
        for product in products:
            st.write(product)
            
    elif choice == "Добавить товар":
        st.subheader("Добавить новый товар")
        product_name = st.text_input("Наименование товара")
        product_quantity = st.number_input("Количество", value=0)
        
        if st.button("Добавить"):
            new_product = Product(len(products) + 1, product_name, product_quantity)
            products.append(new_product)
            st.success(f"Товар {product_name} добавлен!")
            
    elif choice == "Создать заявку":
        st.subheader("Создать новую заявку")
        project_name = st.text_input("Название проекта")
        project_number = st.text_input("Номер проекта")
        desired_delivery_date = st.date_input("Желаемая дата поставки")
        selected_product = st.selectbox("Выберите товар", products)
        product_quantity = st.number_input("Количество", value=0)
        
        if st.button("Добавить заявку"):
            new_request = Request(len(requests) + 1, project_name, project_number, desired_delivery_date)
            new_request.add_product(selected_product, product_quantity)
            requests.append(new_request)
            st.success(f"Заявка для проекта {project_name} создана!")
            
    elif choice == "Создать накладную":
        st.subheader("Создать новую накладную")
        invoice_type = st.selectbox("Тип накладной", ["Закупка", "Отгрузка"])
        invoice_date = st.date_input("Дата накладной")
        selected_product = st.selectbox("Выберите товар", products)
        product_quantity = st.number_input("Количество", value=0)
        
        if st.button("Добавить накладную"):
            new_invoice = Invoice(len(invoices) + 1, invoice_type, invoice_date)
            new_invoice.add_product(selected_product, product_quantity)
            invoices.append(new_invoice)
            st.success(f"Накладная {invoice_type} создана!")

if __name__ == "__main__":
    app()
