from django.db import models
from .services.logic import Math, ResultService, UtilityService

class TableOne(models.Model):

    actual_value = models.FloatField(verbose_name=
                                     'Значение на конец отчетного периода',)
    diff_reason = models.CharField(max_length=255,
                                   verbose_name=
                                   'Обоснование отклонения фактического значения',)
    
    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def result(self):
        plan_value = self.init.plan_value
        return ResultService.result(
            plan_value,
            self.actual_value)
    
    @property
    def percentage_deviation(self):
        plan_value = self.init.plan_value
        return Math.calculate_relative_diviation(plan_value,
                                             self.actual_value)


class TableTwo(models.Model):

    rf_actually = models.FloatField(verbose_name='Референс',)
    mb_actually = models.FloatField(verbose_name='МБ',)
    vnb_actually = models.FloatField(verbose_name='ВНБ',)

    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)

    @property
    def planned_sum(self):
        rf_set = self.init.rf_set
        mb_set = self.init.mb_set
        vnb_set = self.init.vnb_set
        return UtilityService.calculate_sums(
            rf_set, mb_set, vnb_set)

    @property
    def actual_sum(self):
        return Math.calculate_ratio_mastered_to_unmastered(
            self.rf_actually, self.mb_actually, self.vnb_actually)


    @property
    def mastered_to_unmastered(self):
        return Math.calculate_ratio_mastered_to_unmastered(
            self.actual_sum, self.planned_sum)

class TableThree(models.Model):

    time_execution_actually = models.FloatField(verbose_name='Время по факту',)
    actual_result = models.CharField(max_length=255, verbose_name='Результат',)
    



class InitialData(models.Model):

    indicator_name = models.CharField(max_length=255,
                                      verbose_name='Наименование целевого индикатора')
    unit = models.CharField(max_length=50,
                            verbose_name='Единица измерения')
    plan_value = models.FloatField(verbose_name='План на текущий год')


    event_name = models.CharField(max_length=255,
                                  verbose_name='Наименование мероприятия')
    rf_set = models.FloatField(verbose_name='Референс',)
    mb_set = models.FloatField(verbose_name='МБ',)
    vnb_set = models.FloatField(verbose_name='ВНБ',)


    time_execution_plan = models.FloatField(verbose_name='Срок выполнения по плану')
    expected_result = models.CharField(max_length=255, verbose_name='Ожидаемы результат',)
