import numpy as np
import os
import control_planning_scene
import rospy
from get_feature import featuremapping
from test_mesh_pickandplace import create_environment
from tqdm import trange



def main():

    # dir_path = os.path.dirname(os.path.abspath(__file__))
    # yy = os.path.join(dir_path,  'sampled_trajectories/planning_trajectory.npz')
    # planning_trajectory = np.load(yy, allow_pickle=True)
    # rospy.init_node("tutorial_ur5e", anonymous=True)



    PHI_A = list()
    PHI_B = list()


    # #print(planning_trajectory['plan'][0])
    # planning_scene_1 = control_planning_scene.control_planning_scene()
    # get_feature_map = featuremapping(planning_scene_1)

            
    # env, grasp_point, approach_direction, objects_co, neutral_position = create_environment(planning_scene_1)


    for i in trange(5000):
        feature_set = np.load('/home/joonhyeok/catkin_ws/src/my_ur5_env/myur5_description/src/preference_based_learning/ctrl_samples/' + 'avoid' + '_features'+'.npz', allow_pickle=True)['features']
        #feature_map = get_feature_map.get_feature(objects_co=objects_co, planning_trajectory=planning_trajectory['plan'][i])
        if i % 2 == 0:
            PHI_A.append(feature_set[i])
        else:
            PHI_B.append(feature_set[i])

    PHI_A = np.array(PHI_A)
    PHI_B = np.array(PHI_B)
    
    
    
    PSI_SET = PHI_A - PHI_B

    #print(feature_map)
    print(len(PHI_B))
    print(len(PHI_A))
    print(len(PSI_SET))

    print(PHI_A[0])
    print(PHI_B[0])
    print(PSI_SET[0])
    data = np.load('/home/joonhyeok/catkin_ws/src/my_ur5_env/myur5_description/src/preference_based_learning/ctrl_samples/' + 'avoid' + '.npz', allow_pickle=True)
    inputs_set = data['inputs_set']
    
    np.savez('/home/joonhyeok/catkin_ws/src/my_ur5_env/myur5_description/src/preference_based_learning/ctrl_samples/' + 'avoid' + '.npz' ,psi_set=PSI_SET, inputs_set=inputs_set)


def main2():
    
    # dir_path = os.path.dirname(os.path.abspath(__file__))
    # yy = os.path.join(dir_path,  'sampled_trajectories/planning_trajectory.npz')
    # planning_trajectory = np.load(yy, allow_pickle=True)
    # rospy.init_node("tutorial_ur5e", anonymous=True)


    data = np.load('/home/joonhyeok/catkin_ws/src/my_ur5_env/myur5_description/src/preference_based_learning/ctrl_samples/' + 'avoid' + '.npz', allow_pickle=True)
    inputs_set = data['inputs_set']


    features_data = np.load('/home/joonhyeok/catkin_ws/src/my_ur5_env/myur5_description/src/preference_based_learning/ctrl_samples/' + 'avoid' + '_features'+'.npz', allow_pickle=True)
    predefined_features = features_data['features']


    print(inputs_set.shape)
    print(predefined_features.shape)
    # # #print(planning_trajectory['plan'][0])
    # planning_scene_1 = control_planning_scene.control_planning_scene()
    # get_feature_map = featuremapping(planning_scene_1)

            
    # env, grasp_point, approach_direction, objects_co, neutral_position = create_environment(planning_scene_1)


    # for i in trange(200):
    #     feature_map = get_feature_map.get_feature(objects_co=objects_co, planning_trajectory=planning_trajectory['plan'][i])
    #     if i % 2 == 0:
    #         PHI_A.append(feature_map)
    #     else:
            #PHI_B.append(feature_map)

    # PHI_A = np.array(PHI_A)
    # PHI_B = np.array(PHI_B)
    
    
    
    # PSI_SET = PHI_A - PHI_B

    # #print(feature_map)
    # print(len(PHI_B))
    # print(len(PHI_A))
    # print(len(PSI_SET))

    # print(PHI_A[0])
    # print(PHI_B[0])
    # print(PSI_SET[0])
    
    
    # np.savez("./sampled_trajectories/psi_set.npz", PHI_A=PHI_A, PHI_B=PHI_B, PSI_SET=PSI_SET)



if __name__ == "__main__":
    main()