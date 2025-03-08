#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: federico
"""

import sys 
import math
from PyQt5 import QtWidgets 
from GUI import Ui_MainWindow
import matplotlib.pyplot as plt                                                 
import numpy as np
from pyfiglet import figlet_format

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self) 
        Ui_MainWindow.__init__(self) 
        self.setupUi(self) 
        
        #Asignar parametros a los ComboBox
        lista_cb_p = ['mg / m3', 'µg / L']
        self.cb_p.addItems(lista_cb_p)
        
        lista_cb_t = ['hours', 'days', 'years']
        self.cb_t.addItems(lista_cb_t)
        
        lista_cb_le = ['t', 'kt', 'Mt']
        self.cb_le.addItems(lista_cb_le)
        
        lista_cb_v = ['dam3', 'hm3', 'km3']
        self.cb_v.addItems(lista_cb_v)
        
        lista_cb_qs = ['m3 / s', 'dam3 / s', 'hm3 / s']
        self.cb_qs.addItems(lista_cb_qs)
               
        lista_cb_sr = ['µm', 'mm', 'cm']
        self.cb_sr.addItems(lista_cb_sr)        
        
        lista_cb_ad = ['cm', 'm']
        self.cb_ad.addItems(lista_cb_ad)   
        
        lista_cb_tw = ['days', 'hours']
        self.cb_tw.addItems(lista_cb_tw)   
        
        lista_cb_modelo = ['Bartsch & Gakstatter', 'Rast & Lee', 'Dillon & Rigler']
        self.cb_modelo.addItems(lista_cb_modelo)  
        
        final1 = figlet_format('       Marina' + '\n' + '             v 1.0' , font='small')

        self.resultado.setText(final1)

        self.Calcular.clicked.connect(self.calculos)
        
    def calculos(self): 
        inicial = self.inicial.value()
        caudal = self.caudal.value()
        volumen = self.volumen.value()
        ingreso = self.ingreso.value()
        profundidad = self.profundidad.value()
        sedimentacion = self.sedimentacion.value()
        tiempo = self.t.value()
        tw = self.tw.value()
                
        if self.inicial.value() == 0.0:
            self.inicial.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
        if self.caudal.value() == 0.0:
            self.caudal.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
        if self.volumen.value() == 0.0:
            self.volumen.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
        if self.ingreso.value() == 0.0:
            self.ingreso.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
        if self.profundidad.value() == 0.0:
            self.profundidad.setStyleSheet('color: red')  
            final = "OOOPS! Remember to complete all the variables."
        if self.sedimentacion.value() == 0.0:
            self.sedimentacion.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
        if self.t.value() == 0.0:
            self.t.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
        if self.tw.value() == 0.0:
            self.tw.setStyleSheet('color: red')
            final = "OOOPS! Remember to complete all the variables."
            
        
        if ((self.inicial.value() != 0.0) & (self.caudal.value() != 0.0) & (self.volumen.value() != 0.0) &
            (self.ingreso.value() != 0.0) & (self.profundidad.value() != 0.0) & (self.sedimentacion.value() != 0.0) 
            & (self.t.value() != 0.0) & (self.tw.value() != 0.0)):

            self.inicial.setStyleSheet('color: rgb(1,255,1)')            
            self.caudal.setStyleSheet('color: rgb(1,255,1)')           
            self.volumen.setStyleSheet('color: rgb(1,255,1)')     
            self.ingreso.setStyleSheet('color: rgb(1,255,1)')            
            self.profundidad.setStyleSheet('color: rgb(1,255,1)')           
            self.sedimentacion.setStyleSheet('color: rgb(1,255,1)')          
            self.t.setStyleSheet('color: rgb(1,255,1)')           
            self.tw.setStyleSheet('color: rgb(1,255,1)')             
        
            # Seteo de ingreso
            if self.cb_le.currentText() == "t":
                ingreso = ingreso * 1000
            elif self.cb_le.currentText() == "kt":
                ingreso = ingreso * 1000000
            else:
                ingreso = ingreso * 1000000000
                
            # Seteo de volumen
            if self.cb_v.currentText() == "dam3":
                volumen = volumen * 1000
            elif self.cb_v.currentText() == "hm3":
                volumen = volumen * 1000000
            else:
                volumen = volumen * 1000000000
                
            # Seteo de caudal
            if self.cb_qs.currentText() == "m3 / s":
                caudal = caudal 
            elif self.cb_qs.currentText() == "dam3 / s":
                caudal = caudal * 1000
            else:
                caudal = caudal * 1000000
                
            # Seteo de sedimentacion
            if self.cb_sr.currentText() == "µm":
                sedimentacion = sedimentacion / 1000000 
            elif self.cb_sr.currentText() == "mm":
                sedimentacion = sedimentacion / 1000
            else:
                sedimentacion = sedimentacion / 100      
    
            # Seteo de profundidad
            if self.cb_ad.currentText() == "m":
                profundidad = profundidad 
            else:
                profundidad = profundidad * 100  
            
            # Seteo del tiempo
            if self.cb_t.currentText() == "hours":
                tiempo = tiempo / 8766
            elif self.cb_t.currentText() == "days":
                tiempo = tiempo / 365.25
            else:
                tiempo = tiempo     
                
            # Seteo de tw
            if self.cb_tw.currentText() == "hours":
                tw = tw / 24
            else:
                tw = tw    
                                                   
            # Calculos iniciales
            
            # Fósforo
            
            k_año = sedimentacion / profundidad   
            
            k_seg = k_año / 60 / 60 / 24 / 365.25  
            
            tau_seg = volumen / (caudal + k_seg * volumen) 
            
            tau_año = tau_seg / 60 /60 / 24 / 365.25
            
            exponencial = -(tiempo/tau_año)    
            
            ingreso_mg = ingreso * 1000000     
            
            fosforo_total = inicial * math.exp(exponencial) + ((ingreso_mg * tau_año)/volumen) * (1-math.exp(exponencial))        
            
            fosforo_total_st = str(fosforo_total)  + ' ' + 'mg / m3'       
    #        k_st = str(k_seg)
    #        tau_st = str(tau_año)
    #        exponencial_st = str(exponencial)         
            
            # Correccion de fósforo
      
            tiempo2 = 365.25 * tiempo
                    
            exponencial2 = math.pow((tw/tiempo2),0.5)
            
            print ('exponencial: ' , exponencial2)
            
            P = fosforo_total/(1+exponencial2)
                   
            print ('tiempo: ' , tiempo)
            print ('tiempo2: ' , tiempo2)
            print ('fosforo total: ' , fosforo_total)
            print ('fosforo corregido: ' , P)
            
            ### Chl
            
            # Volenweider (Sin usar)
            
    #        chl = 0.37 * math.pow(P,0.79)
    #        chlmax = 0.74 * math.pow(P,0.89)
            
            # Seteo de modelo
            chl = 0
            
            if self.cb_modelo.currentText() == "Bartsch & Gakstatter":
                
                chl = math.pow(10, (0.807 * math.log10(P) - 0.194)) 
                
            elif self.cb_modelo.currentText() == "Rast & Lee":
                
                chl = math.pow(10, (0.760 * math.log10(P) - 0.259))
                
            elif self.cb_modelo.currentText() == "Dillon & Rigler":
                
                chl = math.pow(10, (1.449 * math.log10(P/0.9) - 1.136))   
                
            chl_st = str(chl) + ' ' + 'mg / m3'  
                    
            print ('contenido de clorofila: ' , chl)
               
            # Eutrofización
            
            if chl >= 9:
                
                estado = "eutrophic"
                
            elif  9 > chl > 2.7:
                
                estado = "mesotrophic"
                
            else:
                
                estado = "oligotrophic"
            
            print ('estado de estrofizacion: ' , estado)       
                       
            # Equilibrio
            
            equilibrio_p = ((ingreso_mg * tau_año)/volumen)
            
            equilibrio_chl = 0
            
            if self.cb_modelo.currentText() == "Bartsch & Gakstatter":
                
                equilibrio_chl = math.pow(10, (0.807 * math.log10(equilibrio_p) - 0.194)) 
                
            elif self.cb_modelo.currentText() == "Rast & Lee":
                
                equilibrio_chl = math.pow(10, (0.760 * math.log10(equilibrio_p) - 0.259))
                
            elif self.cb_modelo.currentText() == "Dillon & Rigler":
                
                equilibrio_chl = math.pow(10, (1.449 * math.log10(equilibrio_p/0.9) - 1.136))   
            
            equilibrio_p_st = str(equilibrio_p) + ' ' + 'mg / m3'  
            
            equilibrio_chl_st = str(equilibrio_chl) + ' ' + 'mg / m3'  
            
            print ('cantidad de fosforo para llegar al equilibrio: ' , equilibrio_p)
            print ('cantidad de clorofila para llegar al equilibrio: ' , equilibrio_chl)
            
            if equilibrio_chl >= 9:
                
                estado_eq = "eutrophic"
                
            elif  9 > equilibrio_chl > 2.7:
                
                estado_eq = "mesotrophic"
                
            else:
                
                estado_eq = "oligotrophic"
                
            print ('estado del lago en equilibrio: ' , estado_eq)
                    
            
            # Capacidad máxima de soporte de fósforo al sistema
        
            if self.cb_modelo.currentText() == "Bartsch & Gakstatter":
                
                chlcarga_max = math.pow(10,(((math.log10(9) / math.log10(10)) + 0.194)/0.807))
                            
            elif self.cb_modelo.currentText() == "Rast & Lee":
                
                chlcarga_max = math.pow(10,(((math.log10(9) / math.log10(10)) + 0.259)/0.760))
                
            elif self.cb_modelo.currentText() == "Dillon & Rigler":
                
                chlcarga_max = (math.pow(10,(((math.log10(9) / math.log10(10)) + 1.136)/1.449))) * 0.9
            
            
            P_carga_max = chlcarga_max * (1+exponencial2)
           
            cargamax = ((P_carga_max - inicial * math.exp(exponencial) / (1-math.exp(exponencial)) ) * volumen) / tau_año         
            
            cargamax_total = (chlcarga_max * volumen) / tau_año         
            
            cagamax_total_st =  str(cargamax_total / 1000000000000) + ' ' + 'kt de P'    
    
            print("Cargas maximas")
            print(chlcarga_max)    
            print (cargamax_total)
            
            
                    
            # Gráficos
    
            x = np.linspace(0,tiempo,50)
            y = inicial * np.exp(-(x/tau_año)) + ((ingreso_mg * tau_año)/volumen) * (1-np.exp(-(x/tau_año)))      
            
            tiempo2 = 365.25 * x              
            exponencial2 = np.power((tw/tiempo2),0.5)
            P = fosforo_total/(1+exponencial2)       
            
            if self.cb_modelo.currentText() == "Bartsch & Gakstatter":
                
                z = np.power(10, (0.807 * np.log10(P) - 0.194)) 
                
            elif self.cb_modelo.currentText() == "Rast & Lee":
                
                z = np.power(10, (0.760 * np.log10(P) - 0.259))
                
            elif self.cb_modelo.currentText() == "Dillon & Rigler":
                
                z = np.power(10, (1.449 * np.log10(P/0.9) - 1.136)) 
            
            with plt.style.context('dark_background'):
                plt.plot (x,y,'r-o', label="PT")
                plt.plot (x,z,'b-o', label="Chl")
                plt.axhline(y=9, color='#006400', linestyle='--', label="eutrophic")
                plt.axhline(y=2.7, color='#7CFC00', linestyle='--', label="mesotrophic")  
                plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
    
            plt.show()
                   
        
            # Informe
            
            final = ('### RESULT ###' + '\n\n' +'PT: ' + fosforo_total_st + '\n\n' + 'Chl-ɑ: ' + chl_st + '\n\n'
                     + 'Condition: ' + estado + '\n\n' + '### BALANCE ###' + '\n\n' +'Balance PT: ' + equilibrio_p_st + '\n\n' +
                     'Balance Chl-ɑ: ' + equilibrio_chl_st + '\n\n' +
                     'Balance condition: ' + estado_eq + '\n\n' + '### MAXIMUM PT CAPACITY ###' + '\n\n' + 'Le max: ' + cagamax_total_st)
            
        self.resultado.setText(final)
         
if __name__ == "__main__": 
            app = QtWidgets.QApplication(sys.argv) 
            window = MyApp() 
            window.show() 
            app.exec_()
            
