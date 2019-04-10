
# coding: utf-8

# In[ ]:

import logging, os
import logging.config

def init_logger():
    
    logging.basicConfig()
    logging.config.fileConfig(os.path.abspath('../config/logging.conf'))
     


# In[ ]:

def getlabelname(i):
             
    casestmt = {
         0: 'Billing',
         1: 'Clinic/Doctors Office',
         2: 'Employment',
         3: 'Hospitalization',
         4: 'Insurance/Disability',
         5: 'Military',
         6: 'NRLs',         
         7: 'CardiacData',
         8: 'Consents',
         9: 'Correspondence',
        10: 'EmergencyRoomRecord',
        11: 'Insurance/DisabilityCorrespondence',
        12: 'LaboratoryReports',
        13: 'NaN',
        14: "Nurses' Notes/Telephone Logs",
        15: 'Physicians/Orders',
        16: 'Prescriptions/MedicationLists',
        17: 'ProgressNotes',
        18: "X-Rays/MRIs/CTscansRadiologyQuestionnaries"
   }
    
    return(casestmt.get(i,'lnvalid label'))


# In[ ]:

def writetofile(dataframe,filetowrite):
    dataframe.to_csv(filetowrite)

