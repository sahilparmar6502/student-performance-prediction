

def transform(age,gender,school_type,parent_education,study_hours,attendance_percentage,internet_access,travel_time,extra_activities,study_method,math_score,science_score,english_score,overall_score):

    sample = [age, study_hours, attendance_percentage, math_score, science_score, english_score, overall_score]
    sample += travel_time_encode(travel_time)
    sample += gender_encode(gender)
    sample += school_type_encode(school_type)
    sample += parent_eduction_encode(parent_education)
    sample += internet_access_encode(internet_access)
    sample += extra_activities_encode(extra_activities)
    sample += study_method_encode(study_method)

    return sample

def travel_time_encode(travel_time):

     if travel_time =="<15 min": return [7.5]
     elif travel_time ==   "15-30 min": return [22.5]
     elif travel_time ==   "30-60 min": return [45]
     elif travel_time ==   ">60 min": return [75]

def gender_encode(gender):

    if(gender == 'male'): return [1,0]
    elif(gender == 'other'): return [0,1]
    return [0,0]

def school_type_encode(school_type):
    return [1] if school_type == 'private' else [0]

def parent_eduction_encode(parent_education):

    if parent_education == 'No formal': return [0]
    elif parent_education == 'High school': return [1]
    elif parent_education == 'Diploma': return [2]
    elif parent_education == 'Graduate': return [3]
    elif parent_education == 'Post graduate': return [4]
    elif parent_education == 'PhD': return [5]

def internet_access_encode(internet_access):
    return [1] if internet_access == 'Yes' else [0]

def extra_activities_encode(extra_activities):
    return [1] if extra_activities == 'Yes' else [0]

def study_method_encode(study_method):

    if study_method == "textbook": return [0,0,0,0,1]
    elif study_method ==     "notes": return [0,0,1,0,0]
    elif study_method ==     "online videos": return [0,0,0,1,0]
    elif study_method ==     "group study": return [1,0,0,0,0]
    elif study_method ==     "coaching": return [0,0,0,0,0]
    elif study_method ==     "mixed" : return [0,1,0,0,0]
    
    # group Study
    # mixed
    # notes
    # online videos
    # textbook
    