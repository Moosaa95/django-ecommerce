from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Class method to create a new category
    @classmethod
    def create_category(cls, name, description='', image=None):
        """
        Creates a new category with the given name, description, and optional image.
        
        Args:
            name (str): The name of the category (must be unique).
            description (str, optional): A description for the category. Defaults to an empty string.
            image (ImageField, optional): An image for the category. Defaults to None.

        Returns:
            Category: The created Category object.
        """
        category = cls.objects.create(
            name=name,
            description=description,
            image=image
        )
        return category

    # Class method to update an existing category
    @classmethod
    def update_category(cls, category_id, name=None, description=None, image=None):
        """
        Updates an existing category based on the given category ID. Only the fields that are provided
        will be updated.
        
        Args:
            category_id (int): The ID of the category to update.
            name (str, optional): The new name for the category. Defaults to None.
            description (str, optional): The new description for the category. Defaults to None.
            image (ImageField, optional): The new image for the category. Defaults to None.

        Returns:
            Category or None: The updated Category object if successful, or None if the category is not found.
        """
        try:
            category = cls.objects.get(id=category_id)  # Attempt to retrieve the category by ID
            if name:
                category.name = name  # Update name if provided
            if description:
                category.description = description  # Update description if provided
            if image:
                category.image = image  # Update image if provided
            category.save()  # Save the changes to the database
            return category
        except cls.DoesNotExist:
            return None  # Return None if the category does not exist

    # Class method to list all categories
    @classmethod
    def list_categories(cls):
        """
        Retrieves all categories from the database.
        
        Returns:
            QuerySet: A QuerySet containing all Category objects in the database.
        """
        return cls.objects.all()  # Return all categories

    # Class method to retrieve a category by its ID
    @classmethod
    def retrieve_category(cls, category_id):
        """
        Retrieves a category based on its unique category ID.
        
        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            Category or None: The Category object if found, or None if the category does not exist.
        """
        try:
            category = cls.objects.get(id=category_id)  # Attempt to retrieve the category by ID
            return category
        except cls.DoesNotExist:
            return None  # Return None if the category does not exist

    # Class method to delete a category
    @classmethod
    def delete_category(cls, category_id):
        """
        Deletes a category based on its unique category ID.
        
        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            bool: True if the category was successfully deleted, or False if the category was not found.
        """
        try:
            category = cls.objects.get(id=category_id)  # Attempt to retrieve the category by ID
            category.delete()  # Delete the category from the database
            return True  # Return True if the category was successfully deleted
        except cls.DoesNotExist:
            return False  # Return False if the category does not exist