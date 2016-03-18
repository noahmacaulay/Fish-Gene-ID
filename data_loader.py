#def load_data():
    # Return all data in the following format: 
    #
    
ac_m_z = open("ACGene_MGene_ZGene.csv", 'r')
ac_info = open("AtlanticCod_Gene_Info.csv", 'r')
ac_groups = open("AcModuleGOFDR_DataInput.csv", 'r')

ac_up_data = open("AcGeneGO_UpPropagated_DataInput.csv", 'r')
m_up_data = open("MGeneGO_UpPropagated_DataInput.csv", 'r')
z_up_data = open("ZGeneGO_UpPropagated_DataInput.csv", 'r')

ACGene_MGene_ZGene = []
AC_Up_Data = []
M_Up_Data = []
Z_Up_Data = []
AC_Gene_List = []
Group_List = []

for line in ac_m_z:
    spl = line.split(",")
    spl[2] = spl[2].translate(None, '\n') #Delete \ns
    ACGene_MGene_ZGene.append(spl)

for line in ac_up_data:
    spl = line.split(",")
    spl[len(spl) - 1] = spl[len(spl) - 1].translate(None, '\n') #Delete \ns
    AC_Up_Data.append(spl)

AC_Gene_ID = AC_Up_Data[0]
    
for line in m_up_data:
    spl = line.split(",")
    spl[len(spl) - 1] = spl[len(spl) - 1].translate(None, '\n') #Delete \ns
    M_Up_Data.append(spl)
        
M_Gene_ID = M_Up_Data[0]
        
for line in z_up_data:
    spl = line.split(",")
    spl[len(spl) - 1] = spl[len(spl) - 1].translate(None, '\n') #Delete \ns
    Z_Up_Data.append(spl)
    
Z_Gene_ID = Z_Up_Data[0]
    
for line in ac_info:
    spl = line.split(",")
    spl[len(spl) - 1] = spl[len(spl) - 1].translate(None, '\n') #Delete \ns
    AC_Gene_List.append(spl)
        

        
for line in ac_groups:
    spl = line.split(",")
    spl[len(spl) - 1] = spl[len(spl) - 1].translate(None, '\n') #Delete \ns
    Group_List.append(spl)
    
Group_Gene_ID = Group_List[0]

    
    
    
print ACGene_MGene_ZGene[1]


