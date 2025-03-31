import json
import os
from datetime import datetime
import time
from typing import Dict, List

class SeguimientoMetricas:
    """Clase para gestionar el seguimiento de métricas del modelo"""
    def __init__(self, archivo_metricas="Data/metrics.json"):
        self.archivo_metricas = archivo_metricas
        self.metricas = self.cargar_metricas()
        
    def cargar_metricas(self):
        """Carga las métricas desde el archivo JSON"""
        if os.path.exists(self.archivo_metricas):
            try:
                with open(self.archivo_metricas, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self.inicializar_metricas()
        return self.inicializar_metricas()
    
    def inicializar_metricas(self):
        """Inicializa las métricas con valores por defecto"""
        return {
            "total_interactions": 0,
            "rated_interactions": 0,
            "total_rating": 0,
            "average_rating": 0,
            "interactions": [],
            "tiempos_respuesta": []
        }
    
    def guardar_metricas(self):
        """Guarda las métricas en el archivo JSON"""
        os.makedirs(os.path.dirname(self.archivo_metricas), exist_ok=True)
        with open(self.archivo_metricas, 'w', encoding='utf-8') as f:
            json.dump(self.metricas, f, ensure_ascii=False, indent=4)
    
    def agregar_interaccion(self, pregunta, respuesta, calificacion=None):
        """Agrega una nueva interacción y actualiza las métricas"""
        tiempo_inicio = time.time()
        timestamp_pregunta = datetime.now().isoformat()
        
        # Simular un pequeño delay para diferenciar los timestamps
        time.sleep(0.1)
        timestamp_respuesta = datetime.now().isoformat()
        
        interaccion = {
            "pregunta": pregunta,
            "respuesta": respuesta,
            "timestamp_pregunta": timestamp_pregunta,
            "timestamp_respuesta": timestamp_respuesta,
            "calificacion": calificacion,
            "tiempo_procesamiento": round(tiempo_respuesta, 2) if 'tiempo_respuesta' in locals() else 0
        }
        
        self.metricas["interactions"].append(interaccion)
        self.metricas["total_interactions"] += 1
        
        if calificacion is not None:
            self.metricas["rated_interactions"] += 1
            self.metricas["total_rating"] += calificacion
            self.metricas["average_rating"] = self.metricas["total_rating"] / self.metricas["rated_interactions"]
        
        # Calcular y guardar el tiempo de respuesta
        tiempo_fin = time.time()
        tiempo_respuesta = tiempo_fin - tiempo_inicio
        self.metricas["tiempos_respuesta"].append(tiempo_respuesta)
        
        self.guardar_metricas()
    
    def obtener_metricas(self):
        """Retorna las métricas actuales"""
        return {
            "total_interactions": self.metricas["total_interactions"],
            "rated_interactions": self.metricas["rated_interactions"],
            "average_rating": self.metricas["average_rating"],
            "tiempo_respuesta_promedio": round(sum(self.metricas["tiempos_respuesta"]) / len(self.metricas["tiempos_respuesta"]) if self.metricas["tiempos_respuesta"] else 0, 2),
            "ultima_interaccion": self.metricas["interactions"][-1] if self.metricas["interactions"] else None
        } 