#!/bin/bash

### Las líneas #SBATCH configuran los recursos de la tarea
### (aunque parezcan estar comentadas)

### Nombre de la tarea
#SBATCH --job-name=bootstrap_lenstool2

### Cola de trabajos a la cual enviar.
#SBATCH --partition=batch

### Procesos a largar.
### Es OpenMP, o sea que un proceso en un nodo y muchos hilos.
#SBATCH --ntasks=1

### Hilos por proceso
### Poner el mismo valor acá que en OMP_NUM_THREADS/MKL_NUM_THREADS
#SBATCH --cpus-per-task=20

### Tiempo de ejecucion. Formato dias-horas:minutos.
#SBATCH --time 3-0:00

### Script que se ejecuta al arrancar el trabajo

### Cargar el entorno del usuario incluyendo la funcionalidad de modules
### No tocar
. /etc/profile

### Configurar OpenMP/MKL/etc con la cantidad de cores detectada.
export OMP_NUM_THREADS=20
export MKL_NUM_THREADS=20

### Cargar los módulos para la tarea
module load clemente 
module load gcc/
module load cfitsio/3.450
module load gsl/2.5
source activate py2env

### Largar el programa
srun python -u make_boot.py '/mnt/clemente/lensing/MACSJ0416/boot_lenstool/main' -init 50 -ncores 20
