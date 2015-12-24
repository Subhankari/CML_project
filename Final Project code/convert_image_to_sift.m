function[] = extract_sift()
    clear all
    jpg1_files = dir('C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg1/jpg/*.jpg');
    jpg2_files = dir('C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg2/jpg/*.jpg');
    path_jpg1 = 'C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg1/jpg/';
    path_jpg2 = 'C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg2/jpg/';
    wpath_jpg1 = 'C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg1/jpg_normal_features/';
    wpath_jpg2 = 'C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg2/jpg_normal_features/';
    all_features = 'C:/Users/Subhankari/Desktop/desktop_as_on_13th_april/text books/ML/project/ImageRetrieval/Notebook/dataset/jpg1/all_features/all_features';

    for i = 1:length(jpg1_files)
         [pathstr,name,ext] = fileparts(jpg1_files(i).name)
         newpath = strcat(wpath_jpg1,name);
         
        img_path = strcat(path_jpg1,jpg1_files(i).name);
        img_rgb = imread(img_path);
        %image(img_rgb);
        img_gray = rgb2gray(img_rgb);
        %img_singl_prec = im2single(img_gray);
        img_singl_prec = single(img_gray);
        [F,D] = vl_sift(img_singl_prec);
        
        %disp(size(F));
        %disp(ndims(D));
        D = transpose(D);
        [m,n] = size(D);

        for l = 1:m
            for a = 1:n
                disp('D(l,a)');
                disp(D(l,a));
                disp(double(abs(D(l,a)))^(0.5) * double(sign(D(l,a))));
                D(l,a) = double(abs(D(l,a)))^(0.5) * double(sign(D(l,a)));
            end
        end
        
        
        %disp(size(D));
        %disp(img_rgb);
        %imshow(img_gray);
        %if(i > 1)
        %    break;
        %end
        %end
       % dlmwrite(newpath,D,'-append','delimiter',' ','roffset',0)
        %dlmwrite(all_features,D,'-append','delimiter',' ','roffset',0)      
    end
    
     for i = 1:length(jpg2_files)
         [pathstr,name,ext] = fileparts(jpg2_files(i).name)
         newpath = strcat(wpath_jpg2,name);
         
        img_path = strcat(path_jpg2,jpg2_files(i).name);
        img_rgb = imread(img_path);
        %image(img_rgb);
        img_gray = rgb2gray(img_rgb);
        %img_singl_prec = im2single(img_gray);
        img_singl_prec = single(img_gray);
        [F,D] = vl_sift(img_singl_prec);
        
        %disp(size(F));
        %disp(ndims(D));
        D = transpose(D);
        [m,n] = size(D);

        for l = 1:m  
            if l > 1
                break
            end
            for a = 1:n
                disp(double(abs(D(l,a)))^(0.5) * sign(D(l,a)));
                D(l,a) = double(abs(D(l,a)))^(0.5) * sign(D(l,a));
                
            end
        end
        
        %disp(size(D));
        %disp(img_rgb);
        %imshow(img_gray);
        %if(i > 1)
        %    break;
        %end
        %end
        %dlmwrite(newpath,D,'-append','delimiter',' ','roffset',0)
        %dlmwrite(all_features,D,'-append','delimiter',' ','roffset',0)      
    end
    
    
    
%extract_sift()
    
    
