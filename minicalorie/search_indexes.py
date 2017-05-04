import datetime
from haystack import indexes
from minicalorie.models import FoodDes


class FoodDesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, model_attr='comname')

    def get_model(self):
        return FoodDes

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
