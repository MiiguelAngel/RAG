import pandas as pd
import os
from datetime import datetime
from typing import Dict, List

class SeguimientoMetricas:
    """Clase para gestionar el seguimiento de métricas del modelo"""
    def __init__(self, archivo_metricas: str = "data/metrics.csv"):
        self.archivo_metricas = archivo_metricas
        self._asegurar_existencia_archivo()
        
    def _asegurar_existencia_archivo(self):
        """Crea el archivo de métricas si no existe"""
        if not os.path.exists(self.archivo_metricas):
            df = pd.DataFrame(columns=[
                'timestamp', 'query', 'answer', 'rating', 'feedback'
            ])
            df.to_csv(self.archivo_metricas, index=False)
    
    def agregar_interaccion(self, pregunta: str, respuesta: str, calificacion: int = None, retroalimentacion: str = None):
        """Registra una nueva interacción en el archivo de métricas"""
        df = pd.read_csv(self.archivo_metricas)
        nueva_fila = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'query': pregunta,
            'answer': respuesta,
            'rating': calificacion,
            'feedback': retroalimentacion
        }
        df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
        df.to_csv(self.archivo_metricas, index=False)
    
    def obtener_metricas(self) -> Dict:
        """Calcula y retorna las métricas actuales del modelo"""
        if not os.path.exists(self.archivo_metricas):
            return {
                'total_interactions': 0,
                'average_rating': 0,
                'rated_interactions': 0
            }
        
        df = pd.read_csv(self.archivo_metricas)
        df_calificado = df[df['rating'].notna()]
        
        return {
            'total_interactions': len(df),
            'average_rating': df_calificado['rating'].mean() if not df_calificado.empty else 0,
            'rated_interactions': len(df_calificado)
        } 