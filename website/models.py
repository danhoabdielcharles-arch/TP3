from django.db import models # type: ignore
# Dans website/models.py



# ... tes autres modèles existants ...

class Services(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='services/', verbose_name="Image", blank=True, null=True)
    ordre = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        ordering = ['ordre', 'date_creation']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.titre
# Create your models here.



# # # website_page
class Page(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la page")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # Ajout du ManyToManyField avec le modèle intermédiaire
    sections = models.ManyToManyField(
        'Section',
        through='PageSection',  # Indique le modèle à utiliser pour la relation
        related_name='pages'  # Nom pour la relation inverse (Section.pages)
    )

    def __str__(self):
        return f"Page {self.nom} ({self.titre})"


class Section(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la section")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Section {self.nom} ({self.titre})"


class PageSection(models.Model):
    # Clé étrangère vers la Page
    page = models.ForeignKey(
        'Page',
        on_delete=models.CASCADE,
        verbose_name="Page hôte"
    )

    # Clé étrangère vers la Section
    section = models.ForeignKey(
        'Section',
        on_delete=models.CASCADE,
        verbose_name="Section incluse"
    )

    # Champ pour l'ordre de la section dans CETTE page
    ordre = models.PositiveIntegerField(
        verbose_name="Ordre dans la page"
    )

    class Meta:
        # S'assurer qu'une page ne peut avoir qu'une seule section à un ordre donné
        unique_together = (('page', 'ordre'), ('page', 'section'),)

        # Définir l'ordre par défaut pour les requêtes sur ce modèle
        ordering = ['ordre']

    def __str__(self):
        return f"Ordre {self.ordre}: {self.section.nom} dans {self.page.nom}"


class Menu(models.Model):
    libelle = models.CharField(max_length=32, verbose_name="Nom de la menu")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Parent menu")
    url = models.CharField(max_length=255, verbose_name="URL de la menu")
    ordre = models.IntegerField(verbose_name="Ordre de la menu")

    def __str__(self):
        return f"Menu {self.libelle} ({self.url})"

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ['ordre']
        unique_together = [['parent', 'ordre']]


class banner(models.Model):
    PAGE_CHOICES = [
        ('blog', 'blog'),
        ('about', 'about'),
        ('contact', 'Contact'),
        ('gallery', 'gallery'),
        ('pricing', 'pricing'),
        ('team', 'team'),
        ('service-detail', 'service-detail'),
        ('services', 'services'),
        ('index', 'index'),
    ]
    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    titre = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/', blank=True, null=True)

    def __str__(self):
        return f"{self.titre}"
        
class slider(models.Model):
    PAGE_CHOICES = [
        ('index', 'index'),
        ('services', 'services'),
        ('about', 'about'),
    ]
    image = models.ImageField(upload_to='slider/')
    description1 = models.CharField(max_length=120)
    description2 = models.CharField(max_length=120)
    lien = models.URLField(max_length=225, blank=True, null=True)
    mot_lien = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.description1}"
    

class banner3(models.Model):
    PAGE_CHOICES = [
        ('single-blog-post-rightsidebar', 'single-blog-post-rightsidebar'),
        ('single-blog-post-leftsidebar', 'single-blog-post-leftsidebar'),
        ('single-blog-post-withoutsidebar', 'single-blog-post-withoutsidebar'),
    ]
    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    titre = models.CharField(max_length=200)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    date = models.CharField(max_length=155)
    resolution = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titre}"
    
class About(models.Model):
    PAGE_CHOICES = [
        ('about', 'about'),
        ('index', 'index'),
        ('services', 'services'),
    ]

    page = models.CharField(max_length=150, choices=PAGE_CHOICES)
    image = models.ImageField(upload_to='about/')
    intitulé = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    section_title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=150)
    auteur = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titre}"

    class Meta:
        verbose_name = "À propos"
        verbose_name_plural = "À propos"   



class ServiceHeader(models.Model):
    page = models.CharField(max_length=50, default="index")
    small_title = models.CharField(max_length=200, default="START SHIPPING WITH US")
    big_title = models.CharField(max_length=200, default="We are covering all logistics solutions for you")
    subtitle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Header Services ({self.page})"




class ServiceImage(models.Model):
    service = models.ForeignKey(
        Services,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='services/multi/')

    def __str__(self):
        return f"Image pour {self.service.titre}"
    


class FeatureHeader(models.Model):
    PAGE_CHOICES = (
        ('index', 'index'),
        ('services', ' services'),
    )
    
    page = models.CharField(max_length=50, default="index")
    small_title = models.CharField(max_length=200)
    big_title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="features/", blank=True, null=True)

    def __str__(self):
        return f"Features Header ({self.page})"


class FeatureItem(models.Model):
    feature_header = models.ForeignKey(
        FeatureHeader,
        on_delete=models.CASCADE,
        related_name="items"
    )
    titre = models.CharField(max_length=200)
    description = models.TextField()

    ordre = models.IntegerField(default=0)
    image = models.ImageField(upload_to='feature_items/', blank=True, null=True)


    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return self.titre
