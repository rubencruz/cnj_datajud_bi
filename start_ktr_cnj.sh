
cd /home/rubencruzh/Downloads/programas/data-integration/
now=$(date +"%Y-%m-%d.%S.%N")
filename="log_indicador_moodle.$now.log"
 ./kitchen.sh -file "/home/CNJ/dados/ktr/job_cnj.kjb" > /home/CNJ/dados/ktr/logs/$filename
