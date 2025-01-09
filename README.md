# **Ecommerce Website with Django**

This is an eCommerce website built using **Django**, **HTML**, **CSS** (with **Tailwind CSS**), and **JavaScript**. The project is divided into two main sections:

- **Customer-facing app** (`app`): The frontend part of the eCommerce website, where users can browse products, manage their cart, and make purchases.
- **Admin Dashboard app** (`dashboard`): The backend admin panel for managing products, orders, users, and cart data.

## **Features**

### **Customer-facing Features:**

- **User Authentication**: Users can register, log in, and manage their profile.
- **Product Listing**: Display products with details and prices.
- **Product Detail Page**: Detailed page for each product, including a description, price, and an "Add to Cart" option.
- **Shopping Cart**: Users can add products to their cart, view their cart, and proceed to checkout.
- **Checkout Process**: Users can place orders and view their order history.
- **User Profile**: Users can view and update their personal information and order history.

### **Admin Dashboard Features:**

- **Admin Authentication**: Admins can log in to access the dashboard.
- **Product Management**: Admins can add, update, and delete products from the catalog.
- **Order Management**: Admins can view and manage customer orders (e.g., change order status).
- **User Management**: Admins can view and manage user accounts.
- **Cart Management**: Admins can view and manage user carts and abandoned carts.

## **Project Structure**

```bash
ecommerce-project/
├── ecommerce/
│   ├── app/                  # Customer-facing eCommerce app
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── product_list.html
│   │   │   ├── product_detail.html
│   │   │   ├── cart.html
│   │   │   ├── checkout.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── profile.html
│   │   ├── static/
│   │   │   ├── css/
│   │   │   └── js/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   ├── dashboard/            # Admin dashboard app
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── dashboard_base.html
│   │   │   ├── product_dashboard.html
│   │   │   ├── order_dashboard.html
│   │   │   ├── user_dashboard.html
│   │   │   └── cart_dashboard.html
│   │   ├── static/
│   │   │   ├── css/
│   │   │   └── js/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

### **Django Apps Overview**

- **`app`**: The **`app`** handles the customer-facing part of the website.
  - **Models**: Includes models like `Product`, `Cart`, `Order`, and `User`.
  - **Views**: Handles rendering pages like the homepage, product detail page, cart, and checkout.
  - **Templates**: Contains HTML templates for rendering customer-facing pages.
- **`dashboard`**: The **`dashboard`** is for the admin panel.
  - **Models**: Includes models like `Product`, `Order`, `User`, etc., for admin management.
  - **Views**: Handles rendering pages for managing products, orders, users, and carts.
  - **Templates**: Contains HTML templates for rendering the admin dashboard pages.

---

## **Setup Instructions**

### 1. **Clone the repository**

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/ecommerce-project.git
cd ecommerce-project
```

### 2. **Install dependencies**

Set up a virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
pip install -r requirements.txt
```

### 3. **Set up the database**

Run the migrations to set up the database schema:

```bash
python manage.py migrate
```

### 4. **Create a superuser for admin access**

Create a superuser account to access the Django admin panel (used for the dashboard):

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

### 5. **Run the development server**

Now you can start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the customer-facing site and `http://127.0.0.1:8000/admin` to access the admin dashboard.

---

## **Features Implementation**

### **Customer-facing Pages:**

1. **Home Page**: Displays a list of products available for purchase.
2. **Product Detail Page**: Displays detailed information about a selected product.
3. **Cart**: Displays products added to the cart, allowing users to view and modify their cart before checkout.
4. **Checkout**: Allows users to enter their details and place an order.
5. **User Profile**: Allows users to view and update their profile information and order history.

### **Admin Dashboard Pages:**

1. **Product Management**: Admins can add, update, and delete products.
2. **Order Management**: Admins can view all orders and change their statuses (e.g., pending, shipped, delivered).
3. **User Management**: Admins can view, activate, deactivate, or delete user accounts.
4. **Cart Management**: Admins can view and manage abandoned or pending carts.

---

## **Contributing**

We welcome contributions to the project! If you want to contribute, please follow these steps:

### 1. **Fork the repository**

Click the "Fork" button on the top-right of this page to create a copy of the repository in your GitHub account.

### 2. **Create a new branch**

Create a new branch for the feature you are working on:

```bash
git checkout -b feature/<feature-name>
```

### 3. **Work on the feature**

Make changes to the code, add new features, or fix bugs.

### 4. **Commit your changes**

After making changes, commit them with a clear message:

```bash
git add .
git commit -m "Add <feature-name>"
```

### 5. **Push to your fork**

Push your changes to your forked repository:

```bash
git push origin feature/<feature-name>
```

### 6. **Create a Pull Request**

Go to your GitHub repository and click on "Compare & Pull Request" to create a pull request (PR) to merge your changes into the main repository.

---

## **GitHub Workflow**

### **Branches:**

- `main`: Stable production code.
- `dev`: Ongoing development.
- `feature/<feature-name>`: For specific tasks like `feature/product-management`, `feature/order-management`, etc.

### **Issues:**

Create issues for each feature or bug. Examples:

- **Issue 1**: "Create Product Management Dashboard"
- **Issue 2**: "Implement User Authentication for Admin"
- **Issue 3**: "Set Up Order Management Dashboard"
- **Issue 4**: "Create Cart Management Dashboard"

### **Labels:**

- **`feature`**: For new features.
- **`bug`**: For bug fixes.
- **`enhancement`**: For improvements.
- **`help wanted`**: For tasks that require assistance.

### **Pull Requests:**

Each feature or bug fix should be submitted as a pull request. Use the following template:

```markdown
### Description

- Implemented the product management dashboard where admins can add, update, and delete products.

### Tasks Completed

- Created views for adding, updating, and deleting products.
- Created templates for the product management dashboard.

### Screenshots

- Include screenshots or GIFs of the changes made.

### Related Issues

- Closes #<issue-number>
```

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
