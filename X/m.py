U
    b�O_�  �                   @   sz   d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ dZdZdZ	dZ
dZdZd	d
� Zdd� ZdZdd� Ze�  dS )�    N)�sleepz[1;31mz[1;32mz[1;33mz[1;36mz[1;37mz[1;35mc                   C   s   t d� td� d S )Nz[1;32mPlease wait...�   )�printr   � r   r   �m.py�tik
   s    r   c                 C   s0   | d D ]"}t j�|� t j��  td� qd S )N�
g����MbP?)�sys�stdout�write�flushr   )�i�xr   r   r   �wr   s     
 r   u�   	[1;33m  ____                      _ _
	 / ___|___  _ __ ___  _ __ (_) | ___   _ __  _   _
	| |   / _ \| '_ ` _ \| '_ \| | |/ _ \ | '_ \| | | |
	| |__| (_) | | | | | | |_) | | |  __/ | |_) | |_| |
	 \____\___/|_| |_| |_| .__/|_|_|\___| | .__/ \__, |
	                     |_|              |_|    |___/ 
[1;36m╔═══════════════════════════════════════════════════════╗
[1;36m║ 	[1;37mAuthor  [1;37m: [1;32mMRROBO28[1;36m                   		║
[1;36m║ 	[1;37mgithub  [1;37m: [1;32mhttps://github.con/MRROBO28[1;36m		║
[1;36m║ 	[1;37mYoutube [1;37m: [1;32mTEKTRIKBOT CN[1;36m              		║
[1;36m╚═══════════════════════════════════════════════════════╝
	              [1;36m[[1;41m[1;37mCompile  python3[00m[1;36m]
c            
      C   s�  t �d� tt� z�ttd t d t d t d t d t d t �} ttd t d t d t d t d t �}t�  t	| d	��
� }t|d
d�}t�|�}t�|�}t�|�}t�|�}t	|d��dt|� d �}ttd � W n>   ttd t d t d t d � td� t�  Y nX ttd t d t �}	|	dk�rXt�  n:|	dk�r�ttd � td� ttd � td� t��  d S )N�clearzEx :/path/file.py
�[�+�]z
Input filez > zOutput file�r� �exec�wz�#compile by MRROBO28
#Subcribe chanel TEKTRIKBOT CN
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode(zlib.decompress(z)))))zSucses Compile file�!zFile tidak ada!!!�   zMau compile lagi?z(y/t) : �y�tzThanks for used my script ^_^g      �?z
Exiting...�   )�os�systemr   �banm2�input�h�p�br   �open�read�compile�marshal�dumps�zlib�compress�base64Z	b64encoder   �reprr   �m�kr   �marr	   �exit)
Zinp�oZbkZcpZmdZzl�cbZzbZtarZpilr   r   r   r/      s6    
80



$

r/   )r'   r   �timer	   r+   r)   r   r-   r!   r.   r#   r"   �ur   r   r   r/   r   r   r   r   �<module>   s   0