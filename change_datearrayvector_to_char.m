MainDir = pwd; % "0. Matlab Code" is MainDirection / current folder
DataDirLoad='..\2. ToExtract\';

cd(DataDirLoad);
    [~,FileList] = system('dir /B *_log.mat');
    FileList =textscan(FileList, '%s', 'Delimiter', '\n');
    
 for FileNumber=1:length(FileList{1,1})  
% load data
load(FileList{1,1}{FileNumber,1},'DataContainer'); 
str=FileList{1,1}{FileNumber,1}
time=DataContainer{end,4};
DateString = datestr(time);
DataContainer{end,4} = DateString;
save([DataDirLoad, str],'DataContainer')
 end