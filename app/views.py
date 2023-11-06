from django.shortcuts import render
from joblib import load

model = load('D:/Data project/DATA science/Github/Machine-Learning-Repository/Mushroom dataset/web_app/app/saved_model/Visualization_Poison_recommender.joblib')

def predictor(request):
    return render(request, 'base.html')


def forminfo(request):
    # cap_shape = request.GET['cap-shape']
    # cap_surface = request.GET['cap-surface']
    # cap_color = request.GET['cap-color']
    # bruises = request.GET['bruises']
    # gill_spacing = request.GET['gill-spacing']
    # gill_size = request.GET['gill-size']
    # gill_color = request.GET['gill-color']
    # stalk_shape = request.GET['stalk-shape']
    # stalk_root = request.GET['stalk-root']
    # stalk_surface_above_ring = request.GET['stalk-surface-above-ring']
    # stalk_surface_below_ring = request.GET['stalk-surface-below-ring']
    # stalk_color_above_ring = request.GET['stalk-color-above-ring']
    # stalk_color_below_ring = request.GET['stalk-color-below-ring']
    # veil_type = request.GET['veil-type']
    # veil_color = request.GET['veil-color']
    # ring_number = request.GET['ring-number']
    # ring_type = request.GET['ring-type']
    # spore_print_color = request.GET['spore-print-color']
    # population = request.GET['population']
    # habitat = request.GET['habitat']
    data = {
    'cap-shape': request.GET.get('cap-shape', ''),
    'cap-surface': request.GET.get('cap-surface', ''),
    'cap-color': request.GET.get('cap-color', ''),
    'bruises': request.GET.get('bruises', ''),
    'gill-spacing': request.GET.get('gill-spacing', ''),
    'gill-size': request.GET.get('gill-size', ''),
    'gill-color': request.GET.get('gill-color', ''),
    'stalk-shape': request.GET.get('stalk-shape', ''),
    'stalk-root': request.GET.get('stalk-root', ''),
    'stalk-surface-above-ring': request.GET.get('stalk-surface-above-ring', ''),
    'stalk-surface-below-ring': request.GET.get('stalk-surface-below-ring', ''),
    'stalk-color-above-ring': request.GET.get('stalk-color-above-ring', ''),
    'stalk-color-below-ring': request.GET.get('stalk-color-below-ring', ''),
    'veil-type': request.GET.get('veil-type', ''),
    'veil-color': request.GET.get('veil-color', ''),
    'ring-number': request.GET.get('ring-number', ''),
    'ring-type': request.GET.get('ring-type', ''),
    'spore-print-color': request.GET.get('spore-print-color', ''),
    'population': request.GET.get('population', ''),
    'habitat': request.GET.get('habitat', '')
}
    


    ref_seq = ['cap-shape_bell', 'cap-shape_conical', 'cap-shape_flat',
'cap-shape_knobbed', 'cap-shape_sunken', 'cap-shape_convex',
'cap-surface_fibrous', 'cap-surface_grooves', 'cap-surface_smooth',
'cap-surface_scaly', 'cap-color_buff', 'cap-color_cinnamon',
'cap-color_red', 'cap-color_gray', 'cap-color_brown', 'cap-color_pink',
'cap-color_green', 'cap-color_purple', 'cap-color_white',
'cap-color_yellow', 'bruises_no', 'bruises_bruises',
'gill-attachment_attached', 'gill-attachment_free',
'gill-spacing_close', 'gill-spacing_crowded', 'gill-size_broad',
'gill-size_narrow', 'gill-color_buff', 'gill-color_red',
'gill-color_gray', 'gill-color_chocolate', 'gill-color_black',
'gill-color_brown', 'gill-color_orange', 'gill-color_pink',
'gill-color_green', 'gill-color_purple', 'gill-color_white',
'gill-color_yellow', 'stalk-shape_enlarging', 'stalk-shape_tapering',
'stalk-root_missing', 'stalk-root_bulbous', 'stalk-root_club',
'stalk-root_equal', 'stalk-root_rooted',
'stalk-surface-above-ring_fibrous', 'stalk-surface-above-ring_silky',
'stalk-surface-above-ring_smooth', 'stalk-surface-above-ring_scaly',
'stalk-surface-below-ring_fibrous', 'stalk-surface-below-ring_silky',
'stalk-surface-below-ring_smooth', 'stalk-surface-below-ring_scaly',
'stalk-color-above-ring_buff', 'stalk-color-above-ring_cinnamon',
'stalk-color-above-ring_red', 'stalk-color-above-ring_gray',
'stalk-color-above-ring_brown', 'stalk-color-above-ring_orange',
'stalk-color-above-ring_pink', 'stalk-color-above-ring_white',
'stalk-color-above-ring_yellow', 'stalk-color-below-ring_buff',
'stalk-color-below-ring_cinnamon', 'stalk-color-below-ring_red',
'stalk-color-below-ring_gray', 'stalk-color-below-ring_brown',
'stalk-color-below-ring_orange', 'stalk-color-below-ring_pink',
'stalk-color-below-ring_white', 'stalk-color-below-ring_yellow',
'veil-type_partial', 'veil-color_brown', 'veil-color_orange',
'veil-color_white', 'veil-color_yellow', 'ring-number_none',
'ring-number_one', 'ring-number_two', 'ring-type_evanescent',
'ring-type_flaring', 'ring-type_large', 'ring-type_none',
'ring-type_pendant', 'spore-print-color_buff',
'spore-print-color_chocolate', 'spore-print-color_black',
'spore-print-color_brown', 'spore-print-color_orange',
'spore-print-color_green', 'spore-print-color_purple',
'spore-print-color_white', 'spore-print-color_yellow']

    formatted_data = {}
    for key, value in data.items():
        formatted_key = f"{key}_{value.replace('-', '_')}"
        formatted_data[formatted_key] = value
    
    gen_list = list(formatted_data.keys())

    form_select = []
    for i in ref_seq:
        if i in gen_list:
            form_select.append(1)
        else:
            form_select.append(0)

    pred = model.predict([form_select])
    if pred[0] == 0:
        y_pred = "Edible"
    elif pred[0] == 1:
        y_pred = "Poisons"
    else:
        y_pred = "Error"

    return render(request,'result.html',{'result':y_pred,'data':form_select})
