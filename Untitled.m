%FileData = load('Merged_20180201T230002_20180228T073405_log.mat');
%writematrix('file.csv', FileData);


data=load('Merged_20180201T230002_20180228T073405_log.mat');
%writematrix(Merged_20180201T230002_20180228T073405_log, 'Merged_20180201T230002_20180228T073405_log.csv');

%jsonstr= jsonencode(data);
%fid= fopen('new.json','w');
%fwrite(fid,jsonstr,'char');
%fclose(fid);

%T= struct2table(data)

%A = table2array(T)

%table= cell2table(A( :,4))

%writetable(T,'mydata2.csv')

%dt=data.DataContainer(:,(1:3))
%last = data.DataContainer(: ,4)

%for eachcell = 1:size(last,1)
%    temp= last(eachcell)
%    transpose = cellfun(@transpose,temp,'un',0)
%    name = strcat('signal_',int2str(eachcell),'.csv')
%    fprintf(name)
%    writetable( cell2table(transpose), name, 'writevariablenames', false, 'quotestrings', true)
%end    

%writetable( cell2table(dt), 'myfile1.csv', 'writevariablenames', false, 'quotestrings', true)

%writetable( cell2table(last(1)), 'signal.csv', 'writevariablenames', false, 'quotestrings', true)
cell = data.DataContainer(end,4);
d=cell{1}
%table = cell2table(cell)
%first = cell{1,1}{5,1}
DateString = datestr(d)
%dp = cell2table(cell)

%mat = dp((1:258),1)
%dt = cell2table(cl)
%xlswrite('sai.xlsx',cell)
%xlswrite('result.xlsx',cell,'D1')
%table = cell2table(cell)
%d=table(:,:)
%row1=table(1,1)
%arr=table2array(row1)
%writetable(dt,'table.txt');