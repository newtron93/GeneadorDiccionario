#!/bin/bash

#Variables Generales
eliminar_ceros=false
escribir_salida=false
salida=""

##### CONSTANTES COLORES #####
rojo="\033[0;31m"
verde="\033[0;32m"
azul="\033[0;34m"
magenta="\033[0;35m"
cyan="\033[01;36m"
grisC="\033[0;37m"
gris="\033[1;30m"
rojoC="\033[1;31m"
verdeC="\033[1;32m"
amarillo="\033[1;33m"
azulC="\033[1;34m"
magentaC="\033[1;35m"
cyanC="\033[1;36m"
blanco="\033[1;37m"

clear

mensaje() {
    echo -e "  $rojoC Modo de uso:"
    echo -e " $amarillo$0 [OPCIONES]"
    echo -e " $blanco Ejemplo:$rojoC$0 -z -o Diccionario_Años"
    echo ""
    echo -e "   $azulC Opciones:"
    echo -e "   $cyanC -h, Mostrar esta ayuda"
    echo -e "   $verdeC -z, Omitir ceros en los diccionarios"
    echo -e "   $cyanC -o, Especificar archivo de salida."
    echo ""
    echo ""
    echo -e "$amarillo Este script generará todos los números comprendidos entre los dos valores que introduzcas$blanco"
    echo ""
}

if [ $# -eq 0 ]; then
    mensaje
    exit 1
fi

while getopts "zho:" opcion; do
    case $opcion in
    h)
        echo "Menu de ayuda"
        echo ""
        mensaje
        exit 1
        ;;
    z)
        eliminar_ceros=true
        ;;
    o)
        salida="$OPTARG"
        escribir_salida=true
        ;;
    ?)
        echo "opción $OPTARG no reconocida"
        ;;
    :)
        echo "opción $OPTARG requiere un argumento"
        ;;
    esac
done

shift $((OPTIND - 1))

echo ""
echo ""
echo -e "$verdeC Introduce solo un valor numérico entero"
echo -e "$rojoC"
read -p "          Introduce el numero de inicio:   " numero_actual
read -p "          Introduce el numero de fin:   " numero_final
echo -e "$blanco"

while [ $numero_actual -lt $numero_final ]; do
    echo -e "$azulC Calculando número actual: $verdeC$numero_actual"

    if [ $eliminar_ceros == true ]; then
        if [ $escribir_salida == true ]; then
            echo $numero_actual | tr -d "0" >>/tmp/$salida
        else
            echo $numero_actual | tr -d "0"
        fi
    else
        if [ $escribir_salida == true ]; then
            echo $numero_actual >>/tmp/$salida
        else
            echo $numero_actual
        fi
    fi
    let numero_actual++
done

echo -e "$blanco"

if [ $escribir_salida == true ]; then
    cat /tmp/$salida >$salida
    sleep 2
    rm /tmp/$salida
else
    echo "Solo mostrando datos sin guardar en archivos (parámetro '-o')"
fi

#Script realizado por un batoo...
