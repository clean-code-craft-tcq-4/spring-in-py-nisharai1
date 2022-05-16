import math

def calculateStats(numbers):
  computedStats = {'max':math.nan, 'min': math.nan, 'avg':math.nan}
  if numbers:
    computedStats['max'] = max(numbers)
    computedStats['avg'] = sum(numbers) / len(numbers)
    computedStats['min'] = min(numbers)
   
  return computedStats

class StatsAlerter:
  def __init__(self, maxThreshold, alerts:list):
    self.maxThreshold = maxThreshold
    self.alerts = alerts
  
  def checkAndAlert(self, numbers):
    stats = calculateStats(numbers)
    if stats['max'] > self.maxThreshold:
      for alert in self.alerts:
        if hasattr(alert,'emailSent'):
          alert.emailSent
        elif hasattr(alert,'ledGlows'):
          alert.ledGlows
        else:
          pass
   
class EmailAlert:
  def __init__(self):
    self._emailSent = False
  
  @property
  def emailSent(self):
    return True
  
class LEDAlert:
  def __init__(self):
    self._ledGlows = False
   
  @property
  def ledGlows(self):
    return True
