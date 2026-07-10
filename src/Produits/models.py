from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Produits(models.Model):

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantite = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expire = models.DateField()
    image = models.ImageField(null=True,blank=True,upload_to='produits/')
    

    class Meta:
        ordering = ['-date_ajout']
    

    def status_quantite(self):

        if self.quantite == 0 :
            return 'red'
        elif self.quantite <= 10:
            return 'orange'
        else:
            return 'green'
        
    def __str__(self):
        return f"{self.name} - {self.price} FCFA - Stock: {self.quantite}"
    
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vente(models.Model):

    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    date_achat= models.DateTimeField(auto_now_add=True)
    quantite_vente = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE )
    total_price = models.DecimalField(max_digits= 10, decimal_places=2)

    def __str__(self):
        return self.produit
    
class Facture_client(models.Model):
    Customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantite_vente =models.PositiveIntegerField()
    date_achat= models.DateTimeField(auto_now_add=True)
    total_price = models.ForeignKey(Vente, on_delete= models.CASCADE )
    Produit = models.ForeignKey(Produits, on_delete= models.CASCADE)


    def __str__(self):
        return f" le recue de {self.customer.customer}"