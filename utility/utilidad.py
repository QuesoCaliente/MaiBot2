def formatSeconds(seconds):
    hor=(int(seconds/3600))
    minu=int((seconds-(hor*3600))/60)
    seg=seconds-((hor*3600)+(minu*60))
    if hor == 0 and minu != 0 and seg != 0:
        return f'{minu} minutos {seg} segundos'
    elif hor == 0 and minu != 0 and seg == 0:
        return f'{minu} minutos'
    elif minu == 0:
        return f'{seg} segundos'
    elif seg == 0 and hor !=0 and min != 0:
        return f'{hor} horas {minu} minutos'
    else:
        return f'{hor} horas {minu} minutos {seg} segundos'